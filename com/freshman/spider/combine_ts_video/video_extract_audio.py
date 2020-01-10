import os
from ffmpy3 import FFmpeg
from aip import AipSpeech
from com.freshman.spider.common_util.wavTools import WavTools


class VideoExtractAudio(object):
    def __init__(self, ffmpeg_executable="ffmpeg"):
        self.executable = ffmpeg_executable

    @staticmethod
    def mk_dir_output(output_dir):
        """
        生成目录
        :param output_dir:目录
        :return: 生成是否成功
        """
        is_exists = os.path.exists(output_dir)
        if not is_exists:
            print("创建音频存放目录")
            os.makedirs(output_dir)
            os.chdir(output_dir)
            return True
        else:
            print("目录已经存在，即将保存")
            return True

    def video_to_wav(self, file, out_put_dir):
        """
        视频文件生成音频文件
        :param file: 视频文件路径
        :param out_put_dir: 需要保存音频文件目录
        :return:音频文件路径
        """
        input_file = file
        file_type = file.split('.')[-1]
        file_name = os.path.basename(file)
        VideoExtractAudio.mk_dir_output(out_put_dir)
        out_put_file = os.path.join(out_put_dir, file_name.replace(file_type, 'wav'))
        ff = FFmpeg(executable=self.executable,
                    inputs={input_file: None},
                    global_options=['-y'],
                    outputs={out_put_file: '-vn -ar 16000 -ac 1 -ab 192 -f wav'})
        print(f'将通过命令执行音频文件提取：{ff.cmd}')
        ff.run()
        print(f'提取完成，文件路径：{out_put_file}')
        return out_put_file

    def wav_split(self, audio_file):
        """
        分割音频文件
        :param audio_file:文件路径
        :return: 分割后文件路径
        """
        main_wav_path = audio_file
        path = os.path.dirname(audio_file) + os.path.sep
        # 单位秒
        sound_len = WavTools.get_wav_time(main_wav_path)
        part_file_list = list()
        # 切割文件时长（单位秒）
        part_audio_length = 60
        n = 1
        if sound_len > part_audio_length:
            n = sound_len // part_audio_length
            if n * part_audio_length < sound_len:
                n += 1
        for i in range(int(n)):
            start_time = i * part_audio_length * 1000
            end_time = (i + 1) * part_audio_length * 1000
            if end_time > sound_len * 1000:
                end_time = sound_len * 1000
            part_file_name = f"{path}part_sound_{i}.wav"
            print(f"开始时间{start_time},结束时间{end_time}")
            WavTools.get_ms_part_wav(main_wav_path, start_time, end_time, part_file_name)
            part_file_list.append(part_file_name)
        return part_file_list

    def audio_to_word(self, audio_file):
        """
        从音频中提取文字
        :param audio_file:音频地址
        :return: 文字
        """
        file_content = self.get_file_content(audio_file)
        APP_ID = "XXXXXX"
        API_KEY = "XXXXXXXXXXXXX"
        SECRET_KEY = "XXXXXXXXXXXXXXXXXXX"

        client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

        result = client.asr(file_content, 'wav', 16000, {'dev_pid': 1537})
        if result is None or len(result) < 1:
            print('调用百度api失败')
            return []
        else:
            if result['err_no'] == 0:
                print(f'识别结果：')
                print(result['result'])
                return result['result']
            else:
                print(f"识别错误：{result['err_msg']}")
                return []

    def get_file_content(self, file):
        """
        获取音频文件内容
        :param file: 文件地址
        :return: 文件内容
        """
        if os.path.exists(file):
            with open(file, 'rb') as fp:
                return fp.read()
        return None

    def get_video_core(self, video_file, out_core_dir, core_image_type="jpeg"):
        """
        获取视频关键帧
        :param video_file: 视频文件路径
        :param core_image_type: 图片文件后缀jpeg,png,jpg
        :param out_core_dir: 图片保存目录
        :return:
        """
        input_file = video_file
        file_name = os.path.basename(input_file)
        VideoExtractAudio.mk_dir_output(out_core_dir)
        out_put_file = os.path.join(out_core_dir, file_name + "_%d." + core_image_type)
        ff = FFmpeg(executable=self.executable,
                    inputs={input_file: None},
                    outputs={out_put_file: r"-vf select='eq(pict_type\,I)' -vsync 2 -s 1920*1080 -f image2"})
        print(f'将通过命令执行视频关键帧提取：{ff.cmd}')
        ff.run()
        print(f'提取完成，文件路径：{out_put_file}')


if __name__ == "__main__":
    video_path = os.path.dirname(os.path.realpath(__file__)) + "\\Video\\190318214226685784.mp4"
    audio_dir = os.path.dirname(os.path.realpath(__file__)) + "\\Audio"
    video_core_dir = os.path.dirname(os.path.realpath(__file__)) + "\\Core"
    # FFmpeg的运行目录
    executable = "X:\\FFmpeg\\bin\\ffmpeg.exe"

    # 初始化对象
    video_extract_audio = VideoExtractAudio(ffmpeg_executable=executable)
    # 获取视频关键帧
    video_extract_audio.get_video_core(video_path, video_core_dir)
    # 视频中音频提取
    # audio_path = video_extract_audio.video_to_wav(video_path, audio_dir)
    # 音频切割
    # part_file_list = video_extract_audio.wav_split(audio_path)
    '''for item_part in part_file_list:
        # 音频转为文字
        # video_extract_audio.audio_to_word(item_part)
    '''
    print('处理完成')
