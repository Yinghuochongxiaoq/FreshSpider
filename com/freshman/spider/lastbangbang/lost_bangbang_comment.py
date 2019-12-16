from bs4 import BeautifulSoup
from wordcloud import WordCloud, STOPWORDS
import pandas as pd
import jieba
import matplotlib.pyplot as plt
from pyecharts import Bar, Pie

html = '''
<html><head><title>The Dormouse's story</title></head>
<body><div id="comments" class="comment-list" data-start="100" data-reply_length="90">

  <div class="comment-item" id="9807449" data-cid="9807449" data-user_name="Sapientia" data-user_url="https://www.douban.com/people/183105170/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/183105170/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u183105170-1.jpg" alt="Sapientia"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/183105170/">Sapientia</a>
        <span>2018-08-17 08:37:59</span>
      </div>



      <p class="comment-text">一口一个商业化，自己不也是商业化的附庸吗。我们自己不也是我们想杀死的东西吗？是不是贤者模式我不知道，不食人间烟火怕是家里有矿。何苦可以坚持苦下去，那他身后的团队陪他一起苦下去吗？要不楼主去当摄像试试？外国纪录片大公司赞助钱一抓一大把，中国纪录片筚路蓝缕广告商还得供起来，楼主是否可以拿点矿赞助一下。</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u183105170 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9807449" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9807488" data-cid="9807488" data-user_name="Leopard" data-user_url="https://www.douban.com/people/97158601/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/97158601/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u97158601-4.jpg" alt="Leopard"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/97158601/">Leopard</a>
        <span>2018-08-17 08:54:04</span>
      </div>



      <p class="comment-text">电影观众没有义务在观影前先看纪录片</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u97158601 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9807488" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9807992" data-cid="9807992" data-user_name="抹茶" data-user_url="https://www.douban.com/people/153060989/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/153060989/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u153060989-2.jpg" alt="抹茶"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/153060989/">抹茶</a>
        <span>2018-08-17 10:45:27</span>
      </div>



      <p class="comment-text">呵呵</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u153060989 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9807992" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9808218" data-cid="9808218" data-user_name="高志鑫" data-user_url="https://www.douban.com/people/183076905/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9757339">
    <div class="avatar left">
        <a href="https://www.douban.com/people/183076905/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u183076905-1.jpg" alt="高志鑫"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/183076905/">高志鑫</a>
        <span>2018-08-17 11:26:22</span>
      </div>



        <div class="reply-quote">
          <span class="short">谢谢你的回复，暴露了你的粗鲁！一个张口就说脏话的人，连我说什么都看不懂的人，嗯，我现在...</span>
          <span class="all">谢谢你的回复，暴露了你的粗鲁！一个张口就说脏话的人，连我说什么都看不懂的人，嗯，我现在不奇怪为什么一部大家都说好的电影你却评价如此之低了，猫眼里打四分那个人应该也是你吧～你的言行暴露了你的修养素质品味，以后我不会再与你对话～最后表达一个观点，我不管它是纪录片还是爱情片还是商业片还是………………只要好看，只要能让我有思考，能打动我，我就喜欢～我接受一切新的创意和手法！我相信大家也会一样，你不接受没关系，别看就好了，谢谢！</span>
          <a href="javascript:;" class="toggle_reply">...</a>
          <span class="pubdate"><a href="https://www.douban.com/people/175009559/">立春</a></span>
        </div>


      <p class="comment-text">说得好</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u183076905 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9808218" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9808222" data-cid="9808222" data-user_name="高志鑫" data-user_url="https://www.douban.com/people/183076905/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9758960">
    <div class="avatar left">
        <a href="https://www.douban.com/people/183076905/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u183076905-1.jpg" alt="高志鑫"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/183076905/">高志鑫</a>
        <span>2018-08-17 11:27:27</span>
      </div>



        <div class="reply-quote">
          <span class="short">楼主是个有一点艺术欣赏能力的人，并且有自己的思考，这值得肯定。但借以激烈的言辞，假装自...</span>
          <span class="all">楼主是个有一点艺术欣赏能力的人，并且有自己的思考，这值得肯定。但借以激烈的言辞，假装自己很有想法，也是件让人忍俊不禁的事情。你其实可以看下剧集版，或许会有点别的启发，导演不是专业的，这部纪录片更多的不应该从专业角度看，而是如你所言的无以言表的剧情关怀。</span>
          <a href="javascript:;" class="toggle_reply">...</a>
          <span class="pubdate"><a href="https://www.douban.com/people/154747166/">拾叁</a></span>
        </div>


      <p class="comment-text">没错，一开始何苦就说了他是一个刚退役的军人</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u183076905 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9808222" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9808237" data-cid="9808237" data-user_name="高志鑫" data-user_url="https://www.douban.com/people/183076905/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9759432">
    <div class="avatar left">
        <a href="https://www.douban.com/people/183076905/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u183076905-1.jpg" alt="高志鑫"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/183076905/">高志鑫</a>
        <span>2018-08-17 11:30:31</span>
      </div>



        <div class="reply-quote">
          <span class="short">版权归作者所有，任何形式转载请联系作者。
作者：Acid（来自豆瓣）
来源：https://www.douba...</span>
          <span class="all">版权归作者所有，任何形式转载请联系作者。
作者：Acid（来自豆瓣）
来源：https://www.douban.com/doubanapp/dispatch?uri=/review/9574214/

我觉得首先片子得像样，既尊重拍摄对象，也尊重观众。这种不伦不类垮掉的东西让多少人心生厌恶，你看看短评也能了解一二。你说年轻人去看，或者说孩子去看，他们能看到什么？你难道就给他们看同情？什么叫假装自己有想法？我的想法永远不是假装出来的，我被恶心到就非说不可。你又有什么权利说我假装呢？</span>
          <a href="javascript:;" class="toggle_reply">...</a>
          <span class="pubdate"><a href="https://www.douban.com/people/148323786/">Acid</a></span>
        </div>


      <p class="comment-text">不是让人们同情他们，而是让年轻人知道现在这个光鲜亮丽的社会是是有这些人的一份努力在里面的</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u183076905 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9808237" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9808517" data-cid="9808517" data-user_name="晨风卷耳" data-user_url="https://www.douban.com/people/78645942/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/78645942/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u78645942-6.jpg" alt="晨风卷耳"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/78645942/">晨风卷耳</a>
        <span>2018-08-17 12:24:08</span>
      </div>



      <p class="comment-text">顶 </p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u78645942 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9808517" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9808629" data-cid="9808629" data-user_name="莉是茉莉的莉" data-user_url="https://www.douban.com/people/168637558/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/168637558/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u168637558-1.jpg" alt="莉是茉莉的莉"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/168637558/">莉是茉莉的莉</a>
        <span>2018-08-17 12:49:33</span>
      </div>



      <p class="comment-text">我采访过导演，专门问过最后的汽车是不是植入。负责人的说不是，如果有人记得电影里的车是什么型号（我不懂车所以记不住），可以核实一下是不是最新款。导演说那是两年前的车型了，如果做植入选择一个两年前的车型植入，车企的公关该下岗了吧~说出来是不想大家误会，导演做这部片子还真不是为了赚钱</p>

      <div class="op-lnks">









      </div>

      <div class="group_banned">
        <span class="gact hidden p_u168637558 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9808629" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9808748" data-cid="9808748" data-user_name="Big Elephent" data-user_url="https://www.douban.com/people/151270785/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/151270785/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u151270785-1.jpg" alt="Big Elephent"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/151270785/">Big Elephent</a>
        <span>2018-08-17 13:17:31</span>
      </div>



      <p class="comment-text">何苦导演自主择业以后用一年时间和棒棒同吃同住同劳动，此后一段时间一直在关注他们的生活，你说这是做作？</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u151270785 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9808748" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9809437" data-cid="9809437" data-user_name="憨豆特工" data-user_url="https://www.douban.com/people/183126243/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9793632">
    <div class="avatar left">
        <a href="https://www.douban.com/people/183126243/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u183126243-1.jpg" alt="憨豆特工"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/183126243/">憨豆特工</a>
        <span>2018-08-17 15:55:52</span>
      </div>



        <div class="reply-quote">
          <span class="short">药神我给的分不高，后来考虑到商业性很强很成功还给提了提。反正当时说不好也被疯狂骂了……...</span>
          <span class="all">药神我给的分不高，后来考虑到商业性很强很成功还给提了提。反正当时说不好也被疯狂骂了……但跟这个片子比药神至少是及格的。</span>
          <a href="javascript:;" class="toggle_reply">...</a>
          <span class="pubdate"><a href="https://www.douban.com/people/148323786/">Acid</a></span>
        </div>


      <p class="comment-text">我只是想问问你，你懂电影不？我想这个导演也很无奈。如果结尾不这么搞一下能不能过终审？龙标能不能拿到？你想过这些没有？不要冲动，劝你最好还是先去看看13集纪录片，了解了解再来评价。不了解就没有发言权。说了水军我觉得都过分了。如果在红卫兵时代估计你就是那傻儿样的红卫兵头子。</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u183126243 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9809437" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9809461" data-cid="9809461" data-user_name="憨豆特工" data-user_url="https://www.douban.com/people/183126243/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9806124">
    <div class="avatar left">
        <a href="https://www.douban.com/people/183126243/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u183126243-1.jpg" alt="憨豆特工"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/183126243/">憨豆特工</a>
        <span>2018-08-17 16:03:00</span>
      </div>



        <div class="reply-quote">
          <span class="short">偏激了，有点情绪在里面。 很多人都是我这个看法，我就想发个长评说说。</span>
          <span class="all">偏激了，有点情绪在里面。 很多人都是我这个看法，我就想发个长评说说。</span>
          <span class="pubdate"><a href="https://www.douban.com/people/148323786/">Acid</a></span>
        </div>


      <p class="comment-text">我在想结尾的确不是很多人喜欢的，如果不植入，你们能看到电影版的吗？我猜想这也不是导演想植入。是谁想植入我想大家都懂的，没有相关部门审批不可能就能上映的，懂了哈？</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u183126243 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9809461" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9809603" data-cid="9809603" data-user_name="热气老青年" data-user_url="https://www.douban.com/people/hot_air/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/hot_air/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u32842549-6.jpg" alt="热气老青年"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/hot_air/">热气老青年</a>  (总是被生活捉弄)
        <span>2018-08-17 16:33:57</span>
      </div>



      <p class="comment-text">我看完lz的差评和所有有理的或无理的回复，表示更加支持lz，但不是支持所说的内容和评分，而是支持他有打差评的权利。</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u32842549 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9809603" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9810152" data-cid="9810152" data-user_name="第二口蛋糕的滋" data-user_url="https://www.douban.com/people/155931300/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/155931300/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u155931300-1.jpg" alt="第二口蛋糕的滋"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/155931300/">第二口蛋糕的滋</a>
        <span>2018-08-17 18:18:32</span>
      </div>



      <p class="comment-text">豆瓣装逼的人有一个特点，不会好好说话。</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u155931300 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9810152" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9810346" data-cid="9810346" data-user_name="Memory" data-user_url="https://www.douban.com/people/165411608/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/165411608/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u165411608-1.jpg" alt="Memory"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/165411608/">Memory</a>
        <span>2018-08-17 18:57:50</span>
      </div>



      <p class="comment-text">电影版只是让更多人了解重庆棒棒这个群体，</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u165411608 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9810346" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9810358" data-cid="9810358" data-user_name="Memory" data-user_url="https://www.douban.com/people/165411608/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/165411608/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u165411608-1.jpg" alt="Memory"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/165411608/">Memory</a>
        <span>2018-08-17 18:59:34</span>
      </div>



      <p class="comment-text">棒棒这个职业只有重庆才有，待过重庆的就晓得，棒棒这个职业是最辛苦，渝中区的老城区都已拆迁，棒棒可能也会随之消失</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u165411608 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9810358" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9810807" data-cid="9810807" data-user_name="憨豆特工" data-user_url="https://www.douban.com/people/183126243/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/183126243/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u183126243-1.jpg" alt="憨豆特工"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/183126243/">憨豆特工</a>
        <span>2018-08-17 20:41:10</span>
      </div>
      <p class="comment-text">看他们评得这么专业，我严重怀疑他们是水军，我只是个观众，我只管好看不好看，看完还能给我留下点什么！并不懂专业术语。我反复看了五遍十三集纪录片看了两遍电影，并没感觉有他们说的那些，我只是觉得是一部良心之作。好看！当然你们有选择差评的权力，但是我觉得还是要问问自己的良心。你就花那么几十块钱看一次，你这么牛为啥不自己去拍一部这么好的纪录片呢？</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u183126243 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9810807" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9811049" data-cid="9811049" data-user_name="心荒如漠" data-user_url="https://www.douban.com/people/156821661/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9757117">
    <div class="avatar left">
        <a href="https://www.douban.com/people/156821661/"><img width="48" height="48" src="https://img1.doubanio.com/icon/user_normal.jpg" alt="心荒如漠"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/156821661/">心荒如漠</a>
        <span>2018-08-17 21:24:12</span>
      </div>



        <div class="reply-quote">
          <span class="short">他颠覆了人们的常识！打破了纪录片的传统！他就是神话！纪录片可以随便拍！你就是在放屁！</span>
          <span class="all">他颠覆了人们的常识！打破了纪录片的传统！他就是神话！纪录片可以随便拍！你就是在放屁！</span>
          <span class="pubdate"><a href="https://www.douban.com/people/148323786/">Acid</a></span>
        </div>


      <p class="comment-text">打破了纪录片的传统，纪录片有传统吗，纪录片就应该拍苦大仇深吗？纪录片的常识是什么，是真实，是吗？那么电影里面，何苦就是一个棒棒，他挑重物、扛大米等，做棒棒要做的苦力，吃棒棒要吃的饭，睡棒棒要睡的床，忍受棒棒要忍受的一切，这些难道还不够真实？他做棒棒，把其他棒棒无法说出的真实说出来记录下来，这是不尊重棒棒吗？你张口就是放屁，你这样的狂妄，那你按照你的纪录片传统拍一个试试。</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u156821661 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9811049" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9811159" data-cid="9811159" data-user_name="陈杰" data-user_url="https://www.douban.com/people/136945318/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9755514">
    <div class="avatar left">
        <a href="https://www.douban.com/people/136945318/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u136945318-1.jpg" alt="陈杰"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/136945318/">陈杰</a>
        <span>2018-08-17 21:43:23</span>
      </div>



        <div class="reply-quote">
          <span class="short">《二十二》让人在电影院坐都坐不住，你觉得这是导演克制？好电影？我也参加了棒棒首映礼，有...</span>
          <span class="all">《二十二》让人在电影院坐都坐不住，你觉得这是导演克制？好电影？我也参加了棒棒首映礼，有笑点有泪点，全场观众没有人不觉得好！颠覆了过去对纪录片的认识，不枯燥不乏味，最后的广告在我看来也是搞笑的一部分，至于摆拍，我们都看过剧集，前面全是剧集内容，后面交代现状，给人希望！请问你从哪里看出摆拍了？你这种喜欢刻意恶评的人，以后不要看电影了，自己去拍吧～～～</span>
          <a href="javascript:;" class="toggle_reply">...</a>
          <span class="pubdate"><a href="https://www.douban.com/people/175009559/">立春</a></span>
        </div>


      <p class="comment-text">哥，别装逼了好嘛，人家从专业角度来说的，差还不准人说了？你自己物理不及格就骂爱因斯坦神经病？感兴趣可以自己买点书看看，行有行规，没有规矩不成方圆！</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u136945318 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9811159" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9811181" data-cid="9811181" data-user_name="陈杰" data-user_url="https://www.douban.com/people/136945318/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/136945318/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u136945318-1.jpg" alt="陈杰"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/136945318/">陈杰</a>
        <span>2018-08-17 21:46:35</span>
      </div>



      <p class="comment-text">纪录片，各位先搞懂什么是纪录片，然后再来说话，别瞎吵吵，给重庆人丢脸好吧，直接就喷，真够了，你们。</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u136945318 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9811181" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9811191" data-cid="9811191" data-user_name="陈杰" data-user_url="https://www.douban.com/people/136945318/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/136945318/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u136945318-1.jpg" alt="陈杰"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/136945318/">陈杰</a>
        <span>2018-08-17 21:48:05</span>
      </div>



      <p class="comment-text">这张嘴一个你拍了看看，找你们这么说你们都懂你们去拍了看看？</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u136945318 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9811191" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9811204" data-cid="9811204" data-user_name="棒棒甲" data-user_url="https://www.douban.com/people/182003592/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/182003592/"><img width="48" height="48" src="https://img1.doubanio.com/icon/user_normal.jpg" alt="棒棒甲"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/182003592/">棒棒甲</a>
        <span>2018-08-17 21:49:54</span>
      </div>



      <p class="comment-text">傻逼一个！何苦当了13个的棒棒，与他们同吃同住同劳动，他哪里消费棒棒了？电影里你那里看出摆拍了，你见过连口型都对不上的摆拍吗？还有你说广告，老黄的女婿还完了房款，按揭个车，不行吗？那些棒棒师傅们现在的生活普遍过好了，电影呈现了那么多他们的新生活，这些都是广告吗？你懂吗，纪录片追求的是真实，真实，你懂吗？何苦，原本衣食无忧，为了留下历史的映像，为了留下时代的记忆，他拍纪录片做电影就是消费“棒棒师傅”吗，你有社会责任感吗？再过几十年，几百年，当我们的后人看到这么一部片子，可以说价值无限！你竟然说何苦导演消费他们，你的良心何在？心灵极端阴暗的一个人！你将受到历史的唾弃和审判！</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u182003592 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9811204" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9811247" data-cid="9811247" data-user_name="棒棒甲" data-user_url="https://www.douban.com/people/182003592/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9811204">
    <div class="avatar left">
        <a href="https://www.douban.com/people/182003592/"><img width="48" height="48" src="https://img1.doubanio.com/icon/user_normal.jpg" alt="棒棒甲"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/182003592/">棒棒甲</a>
        <span>2018-08-17 21:57:57</span>
      </div>



        <div class="reply-quote">
          <span class="short">傻逼一个！何苦当了13个的棒棒，与他们同吃同住同劳动，他哪里消费棒棒了？电影里你那里看出...</span>
          <span class="all">傻逼一个！何苦当了13个的棒棒，与他们同吃同住同劳动，他哪里消费棒棒了？电影里你那里看出摆拍了，你见过连口型都对不上的摆拍吗？还有你说广告，老黄的女婿还完了房款，按揭个车，不行吗？那些棒棒师傅们现在的生活普遍过好了，电影呈现了那么多他们的新生活，这些都是广告吗？你懂吗，纪录片追求的是真实，真实，你懂吗？何苦，原本衣食无忧，为了留下历史的映像，为了留下时代的记忆，他拍纪录片做电影就是消费“棒棒师傅”吗，你有社会责任感吗？再过几十年，几百年，当我们的后人看到这么一部片子，可以说价值无限！你竟然说何苦导演消费他们，你的良心何在？心灵极端阴暗的一个人！你将受到历史的唾弃和审判！</span>
          <a href="javascript:;" class="toggle_reply">...</a>
          <span class="pubdate"><a href="https://www.douban.com/people/182003592/">棒棒甲</a></span>
        </div>


      <p class="comment-text">李克强总理2014年在重庆肯定了“棒棒”师傅在历史上所做的贡献。把“棒棒”精神上升为“中国精神”的重要一部分。何苦导演身体力行记录了一个时代，你竟然玷污他。你什么东西？一个社会渣宰！</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u182003592 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9811247" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9811334" data-cid="9811334" data-user_name="所致。" data-user_url="https://www.douban.com/people/59330075/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9759429">
    <div class="avatar left">
        <a href="https://www.douban.com/people/59330075/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u59330075-46.jpg" alt="所致。"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/59330075/">所致。</a>  (真实的日子还是一个人过)
        <span>2018-08-17 22:11:28</span>
      </div>



        <div class="reply-quote">
          <span class="short">一个纪录片，借拍摄对象之口打汽车广告，意味着什么？整个老头坐在车前不走的片段都是真实性...</span>
          <span class="all">一个纪录片，借拍摄对象之口打汽车广告，意味着什么？整个老头坐在车前不走的片段都是真实性存疑的。真实性在哪里？
之前的剧集版本应该是表现“人穷志不穷”这个思想吧？为什么电影里疯狂煽情甚至已经到了莫名其妙干涉剧情的程度？你企图让观众疯狂同情，观众也只会是同情。
摆不摆拍正常人心里都有数，广告那个都算是演的了。一个片段让我对整个片子产生怀疑。那个赌徒成为网红那段，那个团队的讨论你告诉我不是演出来的？我无法接受演出来的做作纪录片，相信很多人和我一样。
另外整个片子的结构是垮掉的，尤其后半段。不及格电影还逼着我好评，不可能。
整个影评在就事论事，而且我实在合理的摆出问题。所以别上来给我搞那套流氓逻辑。比如他有多努力，棒棒有多辛苦。
我说出来了只是觉得不说不快，不怕骂。上来就给人扣帽子也没什么好说的了。觉得我装逼就装逼，觉得我没良心就没良心，觉得我脑残就脑残。我就是脑残。我自己承认了你们省得骂了。我就非说不可。</span>
          <a href="javascript:;" class="toggle_reply">...</a>
          <span class="pubdate"><a href="https://www.douban.com/people/148323786/">Acid</a></span>
        </div>


      <p class="comment-text">但是，真的没有打广告。。。。</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u59330075 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9811334" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9811357" data-cid="9811357" data-user_name="心荒如漠" data-user_url="https://www.douban.com/people/156821661/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9803835">
    <div class="avatar left">
        <a href="https://www.douban.com/people/156821661/"><img width="48" height="48" src="https://img1.doubanio.com/icon/user_normal.jpg" alt="心荒如漠"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/156821661/">心荒如漠</a>
        <span>2018-08-17 22:15:58</span>
      </div>



        <div class="reply-quote">
          <span class="short">影评本是立足于电影本身，再谈个人想法，观点，感受，楼主只是正常影评，也很有见解。大家太...</span>
          <span class="all">影评本是立足于电影本身，再谈个人想法，观点，感受，楼主只是正常影评，也很有见解。大家太把自己的意愿强加于他的影评身上。</span>
          <a href="javascript:;" class="toggle_reply">...</a>
          <span class="pubdate"><a href="https://www.douban.com/people/179853490/">段润</a></span>
        </div>


      <p class="comment-text">导演在电影里面就是棒棒，他的想法观点感受就是棒棒的想法观点感受。</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u156821661 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9811357" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9811377" data-cid="9811377" data-user_name="立春" data-user_url="https://www.douban.com/people/175009559/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9811159">
    <div class="avatar left">
        <a href="https://www.douban.com/people/175009559/"><img width="48" height="48" src="https://img1.doubanio.com/icon/user_normal.jpg" alt="立春"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/175009559/">立春</a>
        <span>2018-08-17 22:19:57</span>
      </div>



        <div class="reply-quote">
          <span class="short">哥，别装逼了好嘛，人家从专业角度来说的，差还不准人说了？你自己物理不及格就骂爱因斯坦神...</span>
          <span class="all">哥，别装逼了好嘛，人家从专业角度来说的，差还不准人说了？你自己物理不及格就骂爱因斯坦神经病？感兴趣可以自己买点书看看，行有行规，没有规矩不成方圆！</span>
          <a href="javascript:;" class="toggle_reply">...</a>
          <span class="pubdate"><a href="https://www.douban.com/people/136945318/">陈杰</a></span>
        </div>
      <p class="comment-text">你专业你拍！何苦拍了我们就觉得好！我们不装逼，我们干不了这活！我们也不会指责！不像有的人就知道骂，却啥也拿不出来！行有行规？说得好！国内最高评分纪录片就是这部！打动数千网友的就是这部！有人三年时间看了700多遍的就是这部！什么是规矩？这就是规矩！这部电影有缺点没错，它一共花了2万块钱，你还想来看大片啊？它就是一台破机器随机拍摄的，拍到什么就是什么，声音没录上补配音怎么了？口型对不上怎么了，都不是专业演员，他能对上吗？就因为这你就说造假，呵呵，我是该说你太专业还是说你只适合看大投资多机位完美拍摄没有瑕疵的大作？</p>

      <div class="op-lnks">
        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>
      </div>
      <div class="group_banned">
        <span class="gact hidden p_u175009559 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9811377" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9811398" data-cid="9811398" data-user_name="憨豆特工" data-user_url="https://www.douban.com/people/183126243/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/183126243/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u183126243-1.jpg" alt="憨豆特工"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/183126243/">憨豆特工</a>
        <span>2018-08-17 22:23:40</span>
      </div>



      <p class="comment-text">经鉴定这个叫AciD的人，为专业的水军，别人请来的水军，大家不要理他就行了！让他一个人去哗众取宠。</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>
      </div>
      <div class="group_banned">
        <span class="gact hidden p_u183126243 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9811398" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>
</div>
<div id="comments" class="comment-list" data-start="0" data-reply_length="90">







  <div class="comment-item" id="9755514" data-cid="9755514" data-user_name="立春" data-user_url="https://www.douban.com/people/175009559/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/175009559/"><img width="48" height="48" src="https://img1.doubanio.com/icon/user_normal.jpg" alt="立春"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/175009559/">立春</a>
        <span>2018-08-09 09:51:57</span>
      </div>



      <p class="comment-text">《二十二》让人在电影院坐都坐不住，你觉得这是导演克制？好电影？我也参加了棒棒首映礼，有笑点有泪点，全场观众没有人不觉得好！颠覆了过去对纪录片的认识，不枯燥不乏味，最后的广告在我看来也是搞笑的一部分，至于摆拍，我们都看过剧集，前面全是剧集内容，后面交代现状，给人希望！请问你从哪里看出摆拍了？你这种喜欢刻意恶评的人，以后不要看电影了，自己去拍吧～～～</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u175009559 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9755514" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9756042" data-cid="9756042" data-user_name="立春" data-user_url="https://www.douban.com/people/175009559/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/175009559/"><img width="48" height="48" src="https://img1.doubanio.com/icon/user_normal.jpg" alt="立春"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/175009559/">立春</a>
        <span>2018-08-09 11:58:06</span>
      </div>



      <p class="comment-text">还有，你说何苦不尊重棒棒，消费棒棒，你是怎么说出口的？他为了这个行业为了这些人做过多少事情，你看到了吗？如果没有他，这几位棒棒师傅的老年生活会得到重视吗？何苦过年拿自己的积蓄为几百位棒棒师傅团年，送他们棉大衣，默默做了好几年，你知道吗？你到底有何居心？如果他做的不好，会有那么高的评分么？如果片子不好看，会得到那么多人的认可么？</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u175009559 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9756042" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9757113" data-cid="9757113" data-user_name="Acid" data-user_url="https://www.douban.com/people/148323786/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9756042">
    <div class="avatar left">
        <a href="https://www.douban.com/people/148323786/"><img width="48" height="48" src="https://img1.doubanio.com/icon/u148323786-8.jpg" alt="Acid"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/148323786/">Acid</a>
        <span>2018-08-09 16:10:17</span>
      </div>



        <div class="reply-quote">
          <span class="short">还有，你说何苦不尊重棒棒，消费棒棒，你是怎么说出口的？他为了这个行业为了这些人做过多少...</span>
          <span class="all">还有，你说何苦不尊重棒棒，消费棒棒，你是怎么说出口的？他为了这个行业为了这些人做过多少事情，你看到了吗？如果没有他，这几位棒棒师傅的老年生活会得到重视吗？何苦过年拿自己的积蓄为几百位棒棒师傅团年，送他们棉大衣，默默做了好几年，你知道吗？你到底有何居心？如果他做的不好，会有那么高的评分么？如果片子不好看，会得到那么多人的认可么？</span>
          <a href="javascript:;" class="toggle_reply">...</a>
          <span class="pubdate"><a href="https://www.douban.com/people/175009559/">立春</a></span>
        </div>


      <p class="comment-text">XXX有多努力，你知道吗？虽然我看不懂你在说什么，但你就是放屁。</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u148323786 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9757113" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9757117" data-cid="9757117" data-user_name="Acid" data-user_url="https://www.douban.com/people/148323786/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9755514">
    <div class="avatar left">
        <a href="https://www.douban.com/people/148323786/"><img width="48" height="48" src="https://img1.doubanio.com/icon/u148323786-8.jpg" alt="Acid"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/148323786/">Acid</a>
        <span>2018-08-09 16:11:23</span>
      </div>



        <div class="reply-quote">
          <span class="short">《二十二》让人在电影院坐都坐不住，你觉得这是导演克制？好电影？我也参加了棒棒首映礼，有...</span>
          <span class="all">《二十二》让人在电影院坐都坐不住，你觉得这是导演克制？好电影？我也参加了棒棒首映礼，有笑点有泪点，全场观众没有人不觉得好！颠覆了过去对纪录片的认识，不枯燥不乏味，最后的广告在我看来也是搞笑的一部分，至于摆拍，我们都看过剧集，前面全是剧集内容，后面交代现状，给人希望！请问你从哪里看出摆拍了？你这种喜欢刻意恶评的人，以后不要看电影了，自己去拍吧～～～</span>
          <a href="javascript:;" class="toggle_reply">...</a>
          <span class="pubdate"><a href="https://www.douban.com/people/175009559/">立春</a></span>
        </div>


      <p class="comment-text">他颠覆了人们的常识！打破了纪录片的传统！他就是神话！纪录片可以随便拍！你就是在放屁！</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u148323786 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9757117" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9757339" data-cid="9757339" data-user_name="立春" data-user_url="https://www.douban.com/people/175009559/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/175009559/"><img width="48" height="48" src="https://img1.doubanio.com/icon/user_normal.jpg" alt="立春"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/175009559/">立春</a>
        <span>2018-08-09 17:12:05</span>
      </div>



      <p class="comment-text">谢谢你的回复，暴露了你的粗鲁！一个张口就说脏话的人，连我说什么都看不懂的人，嗯，我现在不奇怪为什么一部大家都说好的电影你却评价如此之低了，猫眼里打四分那个人应该也是你吧～你的言行暴露了你的修养素质品味，以后我不会再与你对话～最后表达一个观点，我不管它是纪录片还是爱情片还是商业片还是………………只要好看，只要能让我有思考，能打动我，我就喜欢～我接受一切新的创意和手法！我相信大家也会一样，你不接受没关系，别看就好了，谢谢！</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u175009559 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9757339" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9757352" data-cid="9757352" data-user_name="孤舟影成双" data-user_url="https://www.douban.com/people/130305926/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/130305926/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u130305926-1.jpg" alt="孤舟影成双"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/130305926/">孤舟影成双</a>
        <span>2018-08-09 17:15:11</span>
      </div>



      <p class="comment-text">楼主傻逼，鉴定完毕</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u130305926 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9757352" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9758960" data-cid="9758960" data-user_name="拾叁" data-user_url="https://www.douban.com/people/154747166/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/154747166/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u154747166-3.jpg" alt="拾叁"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/154747166/">拾叁</a>
        <span>2018-08-10 00:15:54</span>
      </div>



      <p class="comment-text">楼主是个有一点艺术欣赏能力的人，并且有自己的思考，这值得肯定。但借以激烈的言辞，假装自己很有想法，也是件让人忍俊不禁的事情。你其实可以看下剧集版，或许会有点别的启发，导演不是专业的，这部纪录片更多的不应该从专业角度看，而是如你所言的无以言表的剧情关怀。</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u154747166 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9758960" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9759422" data-cid="9759422" data-user_name="Acid" data-user_url="https://www.douban.com/people/148323786/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9758960">
    <div class="avatar left">
        <a href="https://www.douban.com/people/148323786/"><img width="48" height="48" src="https://img1.doubanio.com/icon/u148323786-8.jpg" alt="Acid"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/148323786/">Acid</a>
        <span>2018-08-10 05:52:38</span>
      </div>



        <div class="reply-quote">
          <span class="short">楼主是个有一点艺术欣赏能力的人，并且有自己的思考，这值得肯定。但借以激烈的言辞，假装自...</span>
          <span class="all">楼主是个有一点艺术欣赏能力的人，并且有自己的思考，这值得肯定。但借以激烈的言辞，假装自己很有想法，也是件让人忍俊不禁的事情。你其实可以看下剧集版，或许会有点别的启发，导演不是专业的，这部纪录片更多的不应该从专业角度看，而是如你所言的无以言表的剧情关怀。</span>
          <a href="javascript:;" class="toggle_reply">...</a>
          <span class="pubdate"><a href="https://www.douban.com/people/154747166/">拾叁</a></span>
        </div>


      <p class="comment-text">我说了，讨厌的是电影版。</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u148323786 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9759422" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9759423" data-cid="9759423" data-user_name="Acid" data-user_url="https://www.douban.com/people/148323786/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9757339">
    <div class="avatar left">
        <a href="https://www.douban.com/people/148323786/"><img width="48" height="48" src="https://img1.doubanio.com/icon/u148323786-8.jpg" alt="Acid"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/148323786/">Acid</a>
        <span>2018-08-10 05:54:31</span>
      </div>



        <div class="reply-quote">
          <span class="short">谢谢你的回复，暴露了你的粗鲁！一个张口就说脏话的人，连我说什么都看不懂的人，嗯，我现在...</span>
          <span class="all">谢谢你的回复，暴露了你的粗鲁！一个张口就说脏话的人，连我说什么都看不懂的人，嗯，我现在不奇怪为什么一部大家都说好的电影你却评价如此之低了，猫眼里打四分那个人应该也是你吧～你的言行暴露了你的修养素质品味，以后我不会再与你对话～最后表达一个观点，我不管它是纪录片还是爱情片还是商业片还是………………只要好看，只要能让我有思考，能打动我，我就喜欢～我接受一切新的创意和手法！我相信大家也会一样，你不接受没关系，别看就好了，谢谢！</span>
          <a href="javascript:;" class="toggle_reply">...</a>
          <span class="pubdate"><a href="https://www.douban.com/people/175009559/">立春</a></span>
        </div>


      <p class="comment-text">你说的脏话就是“放屁”？我在模仿你罢了。压根就不想和你讨论。我表达我的观点罢了。</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u148323786 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9759423" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9759429" data-cid="9759429" data-user_name="Acid" data-user_url="https://www.douban.com/people/148323786/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/148323786/"><img width="48" height="48" src="https://img1.doubanio.com/icon/u148323786-8.jpg" alt="Acid"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/148323786/">Acid</a>
        <span>2018-08-10 06:05:37</span>
      </div>



      <p class="comment-text">一个纪录片，借拍摄对象之口打汽车广告，意味着什么？整个老头坐在车前不走的片段都是真实性存疑的。真实性在哪里？<br>之前的剧集版本应该是表现“人穷志不穷”这个思想吧？为什么电影里疯狂煽情甚至已经到了莫名其妙干涉剧情的程度？你企图让观众疯狂同情，观众也只会是同情。<br>摆不摆拍正常人心里都有数，广告那个都算是演的了。一个片段让我对整个片子产生怀疑。那个赌徒成为网红那段，那个团队的讨论你告诉我不是演出来的？我无法接受演出来的做作纪录片，相信很多人和我一样。<br>另外整个片子的结构是垮掉的，尤其后半段。不及格电影还逼着我好评，不可能。<br>整个影评在就事论事，而且我实在合理的摆出问题。所以别上来给我搞那套流氓逻辑。比如他有多努力，棒棒有多辛苦。<br>我说出来了只是觉得不说不快，不怕骂。上来就给人扣帽子也没什么好说的了。觉得我装逼就装逼，觉得我没良心就没良心，觉得我脑残就脑残。我就是脑残。我自己承认了你们省得骂了。我就非说不可。</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u148323786 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9759429" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9759432" data-cid="9759432" data-user_name="Acid" data-user_url="https://www.douban.com/people/148323786/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9758960">
    <div class="avatar left">
        <a href="https://www.douban.com/people/148323786/"><img width="48" height="48" src="https://img1.doubanio.com/icon/u148323786-8.jpg" alt="Acid"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/148323786/">Acid</a>
        <span>2018-08-10 06:15:13</span>
      </div>



        <div class="reply-quote">
          <span class="short">楼主是个有一点艺术欣赏能力的人，并且有自己的思考，这值得肯定。但借以激烈的言辞，假装自...</span>
          <span class="all">楼主是个有一点艺术欣赏能力的人，并且有自己的思考，这值得肯定。但借以激烈的言辞，假装自己很有想法，也是件让人忍俊不禁的事情。你其实可以看下剧集版，或许会有点别的启发，导演不是专业的，这部纪录片更多的不应该从专业角度看，而是如你所言的无以言表的剧情关怀。</span>
          <a href="javascript:;" class="toggle_reply">...</a>
          <span class="pubdate"><a href="https://www.douban.com/people/154747166/">拾叁</a></span>
        </div>


      <p class="comment-text">版权归作者所有，任何形式转载请联系作者。<br>作者：Acid（来自豆瓣）<br>来源：<a href="https://www.douban.com/link2/?url=https%3A%2F%2Fwww.douban.com%2Fdoubanapp%2Fdispatch%3Furi%3D%2Freview%2F9574214%2F">https://www.douban.c<wbr>om/doubanapp/dispatc<wbr>h?uri=/review/957421<wbr>4/</a><br><br>我觉得首先片子得像样，既尊重拍摄对象，也尊重观众。这种不伦不类垮掉的东西让多少人心生厌恶，你看看短评也能了解一二。你说年轻人去看，或者说孩子去看，他们能看到什么？你难道就给他们看同情？什么叫假装自己有想法？我的想法永远不是假装出来的，我被恶心到就非说不可。你又有什么权利说我假装呢？</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u148323786 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9759432" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9759433" data-cid="9759433" data-user_name="Acid" data-user_url="https://www.douban.com/people/148323786/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9757352">
    <div class="avatar left">
        <a href="https://www.douban.com/people/148323786/"><img width="48" height="48" src="https://img1.doubanio.com/icon/u148323786-8.jpg" alt="Acid"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/148323786/">Acid</a>
        <span>2018-08-10 06:15:51</span>
      </div>



        <div class="reply-quote">
          <span class="short">楼主傻逼，鉴定完毕</span>
          <span class="all">楼主傻逼，鉴定完毕</span>
          <span class="pubdate"><a href="https://www.douban.com/people/130305926/">孤舟影成双</a></span>
        </div>


      <p class="comment-text">谢谢谢谢</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u148323786 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9759433" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9759438" data-cid="9759438" data-user_name="Acid" data-user_url="https://www.douban.com/people/148323786/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9756042">
    <div class="avatar left">
        <a href="https://www.douban.com/people/148323786/"><img width="48" height="48" src="https://img1.doubanio.com/icon/u148323786-8.jpg" alt="Acid"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/148323786/">Acid</a>
        <span>2018-08-10 06:21:54</span>
      </div>



        <div class="reply-quote">
          <span class="short">还有，你说何苦不尊重棒棒，消费棒棒，你是怎么说出口的？他为了这个行业为了这些人做过多少...</span>
          <span class="all">还有，你说何苦不尊重棒棒，消费棒棒，你是怎么说出口的？他为了这个行业为了这些人做过多少事情，你看到了吗？如果没有他，这几位棒棒师傅的老年生活会得到重视吗？何苦过年拿自己的积蓄为几百位棒棒师傅团年，送他们棉大衣，默默做了好几年，你知道吗？你到底有何居心？如果他做的不好，会有那么高的评分么？如果片子不好看，会得到那么多人的认可么？</span>
          <a href="javascript:;" class="toggle_reply">...</a>
          <span class="pubdate"><a href="https://www.douban.com/people/175009559/">立春</a></span>
        </div>


      <p class="comment-text">1.高评分是剧集版<br>2.高评分不代表绝对优秀<br>3.纪录片是有底线的<br>4.自己没有鉴赏能力就不要胡乱反问我。这种你从哪儿看出来xxx的话很没营养，就好像你从哪儿看出1+1=2一样。<br>5.你的观后感是你自己的想法，我只是说我为什么不喜欢，碍着你喜欢什么事了？这么激动有什么意义？<br>6.我有一说一，没有一点扒瞎，你管这叫恶意给低分。所以只有给你觉得应该高分的电影高分，给你觉得应该低分的电影低分才叫不恶意是吗？你是标尺？</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u148323786 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9759438" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9759756" data-cid="9759756" data-user_name="立春" data-user_url="https://www.douban.com/people/175009559/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/175009559/"><img width="48" height="48" src="https://img1.doubanio.com/icon/user_normal.jpg" alt="立春"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/175009559/">立春</a>
        <span>2018-08-10 09:01:47</span>
      </div>



      <p class="comment-text">你的鉴赏能力就是显摆自己很有鉴赏能力，这是一部纪实电影，既然要把它搬上大银幕，就必须增加可看性和一定的艺术加工，人家就是买车了，老头就是不同意，这本来就是客观存在的问题！河南确实当了一段时间吃播的网红，这也是真实存在的，怎么就摆拍造假了？你可以对影片有意见，这是你的自由和审美，毕竟这只是两万块钱成本做出来的片子，在拥有一大堆优点的同时肯定有它的缺点，但是请你就事论事！别说什么导演消费棒棒！不尊重拍摄群体！借用你的话，你这是在放屁！</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u175009559 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9759756" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9759788" data-cid="9759788" data-user_name="Acid" data-user_url="https://www.douban.com/people/148323786/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9759756">
    <div class="avatar left">
        <a href="https://www.douban.com/people/148323786/"><img width="48" height="48" src="https://img1.doubanio.com/icon/u148323786-8.jpg" alt="Acid"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/148323786/">Acid</a>
        <span>2018-08-10 09:06:40</span>
      </div>



        <div class="reply-quote">
          <span class="short">你的鉴赏能力就是显摆自己很有鉴赏能力，这是一部纪实电影，既然要把它搬上大银幕，就必须增...</span>
          <span class="all">你的鉴赏能力就是显摆自己很有鉴赏能力，这是一部纪实电影，既然要把它搬上大银幕，就必须增加可看性和一定的艺术加工，人家就是买车了，老头就是不同意，这本来就是客观存在的问题！河南确实当了一段时间吃播的网红，这也是真实存在的，怎么就摆拍造假了？你可以对影片有意见，这是你的自由和审美，毕竟这只是两万块钱成本做出来的放屁，在拥有一大堆优点的同时肯定有它的缺点，但是请你就事论事！别说什么导演消费棒棒！不尊重拍摄群体！借用你的话，你这是在放屁！</span>
          <a href="javascript:;" class="toggle_reply">...</a>
          <span class="pubdate"><a href="https://www.douban.com/people/175009559/">立春</a></span>
        </div>


      <p class="comment-text">你根本没有想明白哪个地方存在不真实，跟你说不清楚。你主观臆断觉得我显摆，那我就显摆了，行吧？你又能怎么样呢？</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u148323786 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9759788" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9759802" data-cid="9759802" data-user_name="立春" data-user_url="https://www.douban.com/people/175009559/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9759788">
    <div class="avatar left">
        <a href="https://www.douban.com/people/175009559/"><img width="48" height="48" src="https://img1.doubanio.com/icon/user_normal.jpg" alt="立春"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/175009559/">立春</a>
        <span>2018-08-10 09:09:42</span>
      </div>



        <div class="reply-quote">
          <span class="short">你根本没有想明白哪个地方存在不真实，跟你说不清楚。你主观臆断觉得我显摆，那我就显摆了，...</span>
          <span class="all">你根本没有想明白哪个地方存在不真实，跟你说不清楚。你主观臆断觉得我显摆，那我就显摆了，行吧？你又能怎么样呢？</span>
          <a href="javascript:;" class="toggle_reply">...</a>
          <span class="pubdate"><a href="https://www.douban.com/people/148323786/">Acid</a></span>
        </div>


      <p class="comment-text">你开心就好啊～善良的人是无法跟恶毒的人建立正常交流的，我懂～</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u175009559 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9759802" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9759805" data-cid="9759805" data-user_name="Acid" data-user_url="https://www.douban.com/people/148323786/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9759756">
    <div class="avatar left">
        <a href="https://www.douban.com/people/148323786/"><img width="48" height="48" src="https://img1.doubanio.com/icon/u148323786-8.jpg" alt="Acid"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/148323786/">Acid</a>
        <span>2018-08-10 09:10:01</span>
      </div>



        <div class="reply-quote">
          <span class="short">你的鉴赏能力就是显摆自己很有鉴赏能力，这是一部纪实电影，既然要把它搬上大银幕，就必须增...</span>
          <span class="all">你的鉴赏能力就是显摆自己很有鉴赏能力，这是一部纪实电影，既然要把它搬上大银幕，就必须增加可看性和一定的艺术加工，人家就是买车了，老头就是不同意，这本来就是客观存在的问题！河南确实当了一段时间吃播的网红，这也是真实存在的，怎么就摆拍造假了？你可以对影片有意见，这是你的自由和审美，毕竟这只是两万块钱成本做出来的放屁，在拥有一大堆优点的同时肯定有它的缺点，但是请你就事论事！别说什么导演消费棒棒！不尊重拍摄群体！借用你的话，你这是在放屁！</span>
          <a href="javascript:;" class="toggle_reply">...</a>
          <span class="pubdate"><a href="https://www.douban.com/people/175009559/">立春</a></span>
        </div>


      <p class="comment-text">版权归作者所有，任何形式转载请联系作者。<br>作者：Acid（来自豆瓣）<br>来源：<a href="https://www.douban.com/link2/?url=https%3A%2F%2Fwww.douban.com%2Fdoubanapp%2Fdispatch%3Furi%3D%2Freview%2F9574214%2F">https://www.douban.c<wbr>om/doubanapp/dispatc<wbr>h?uri=/review/957421<wbr>4/</a><br><br>你要是能报销我去北京的机票请我再看一场，我可以挨一个给你指出来，哪里做作，哪里假，哪里是演出来的，行吗？我又不怕这个。你自己都不肯相信也没听明白是在质疑什么讨论还有什么意义呢？我就是在就事论事啊，我的长评里没有就事论事吗？说缺点不叫就事论事，说优点才算呗？</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u148323786 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9759805" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9759875" data-cid="9759875" data-user_name="立春" data-user_url="https://www.douban.com/people/175009559/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9759805">
    <div class="avatar left">
        <a href="https://www.douban.com/people/175009559/"><img width="48" height="48" src="https://img1.doubanio.com/icon/user_normal.jpg" alt="立春"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/175009559/">立春</a>
        <span>2018-08-10 09:28:03</span>
      </div>



        <div class="reply-quote">
          <span class="short">版权归作者所有，任何形式转载请联系作者。
作者：Acid（来自豆瓣）
来源：https://www.douba...</span>
          <span class="all">版权归作者所有，任何形式转载请联系作者。
作者：Acid（来自豆瓣）
来源：https://www.douban.com/doubanapp/dispatch?uri=/review/9574214/

你要是能报销我去北京的机票请我再看一场，我可以挨一个给你指出来，哪里做作，哪里假，哪里是演出来的，行吗？我又不怕这个。你自己都不肯相信也没听明白是在质疑什么讨论还有什么意义呢？我就是在就事论事啊，我的长评里没有就事论事吗？说缺点不叫就事论事，说优点才算呗？</span>
          <a href="javascript:;" class="toggle_reply">...</a>
          <span class="pubdate"><a href="https://www.douban.com/people/148323786/">Acid</a></span>
        </div>


      <p class="comment-text">你爱看不看～我不需要你告诉我哪里不好，连新闻联播都无法做到完全实时记录事件现场，更何况一部资金都没有像样的海报都做不起的影片呢？你说的那两个摆拍，都是生活中真实发生的故事，我个人感觉有可能导演没有记录到第一现场，所以做了还原呈现在电影里，加上主人公又不是专业演员，所以让你觉得做作，这很正常！我也做过新闻，我不觉得这就说明导演有问题！我感恩导演在这浮躁的社会能静下心来拍摄这样一部好放屁，给我感动思考启迪，还让我在观影过程中有泪有笑，足够了～～～还是那句话，你可以发表你的观点，这是你的自由，我反驳你是因为你说导演不尊重被拍摄者和消费棒棒！</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u175009559 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9759875" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9761266" data-cid="9761266" data-user_name="Acid" data-user_url="https://www.douban.com/people/148323786/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9759802">
    <div class="avatar left">
        <a href="https://www.douban.com/people/148323786/"><img width="48" height="48" src="https://img1.doubanio.com/icon/u148323786-8.jpg" alt="Acid"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/148323786/">Acid</a>
        <span>2018-08-10 13:30:19</span>
      </div>



        <div class="reply-quote">
          <span class="short">你开心就好啊～善良的人是无法跟恶毒的人建立正常交流的，我懂～</span>
          <span class="all">你开心就好啊～善良的人是无法跟恶毒的人建立正常交流的，我懂～</span>
          <span class="pubdate"><a href="https://www.douban.com/people/175009559/">立春</a></span>
        </div>


      <p class="comment-text">辩不明白就人身攻击，牛逼，服气。我恶意评论，我恶毒。谢谢您。</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u148323786 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9761266" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9761283" data-cid="9761283" data-user_name="Acid" data-user_url="https://www.douban.com/people/148323786/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9759875">
    <div class="avatar left">
        <a href="https://www.douban.com/people/148323786/"><img width="48" height="48" src="https://img1.doubanio.com/icon/u148323786-8.jpg" alt="Acid"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/148323786/">Acid</a>
        <span>2018-08-10 13:33:30</span>
      </div>



        <div class="reply-quote">
          <span class="short">你爱看不看～我不需要你告诉我哪里不好，连新闻联播都无法做到完全实时记录事件现场，更何况...</span>
          <span class="all">你爱看不看～我不需要你告诉我哪里不好，连新闻联播都无法做到完全实时记录事件现场，更何况一部资金都没有像样的海报都做不起的影片呢？你说的那两个摆拍，都是生活中真实发生的故事，我个人感觉有可能导演没有记录到第一现场，所以做了还原呈现在电影里，加上主人公又不是专业演员，所以让你觉得做作，这很正常！我也做过新闻，我不觉得这就说明导演有问题！我感恩导演在这浮躁的社会能静下心来拍摄这样一部好放屁，给我感动思考启迪，还让我在观影过程中有泪有笑，足够了～～～还是那句话，你可以发表你的观点，这是你的自由，我反驳你是因为你说导演不尊重被拍摄者和消费棒棒！</span>
          <a href="javascript:;" class="toggle_reply">...</a>
          <span class="pubdate"><a href="https://www.douban.com/people/175009559/">立春</a></span>
        </div>


      <p class="comment-text">纪录片里演戏，还说的冠冕堂皇。</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u148323786 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9761283" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9761449" data-cid="9761449" data-user_name="立春" data-user_url="https://www.douban.com/people/175009559/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9761266">
    <div class="avatar left">
        <a href="https://www.douban.com/people/175009559/"><img width="48" height="48" src="https://img1.doubanio.com/icon/user_normal.jpg" alt="立春"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/175009559/">立春</a>
        <span>2018-08-10 13:52:23</span>
      </div>



        <div class="reply-quote">
          <span class="short">辩不明白就人身攻击，牛逼，服气。我恶意评论，我恶毒。谢谢您。</span>
          <span class="all">辩不明白就人身攻击，牛逼，服气。我恶意评论，我恶毒。谢谢您。</span>
          <span class="pubdate"><a href="https://www.douban.com/people/148323786/">Acid</a></span>
        </div>


      <p class="comment-text">请你搞清楚，十三集的是纪录片，这个是纪实电影！纪实电影！而且是否后面还原场景也只是我个人的推测！不管他是怎么拍的，好看就行，你管人家怎么拍呢？不爱看你别看啊！这样的影片是给内心充满阳光的人看的！不是张口就说“放屁”的粗俗人士看的！还有，你说的植入广告，我告诉你，全篇广告太多太多了，解放碑广场的大屏幕里好多个，第一个镜头里的立邦漆，何苦和老黄无家可归时睡的石头上刻的美心门，老杭头上戴的帽子品牌………一部纪录片怎么能避免掉所有的广告，这些人又不是生活在真空里，他们是生活在这个花花世界里的人！想喷真是什么都可以成为理由！何苦本来就是创新，过去也没有纪录片导演进入角色体验同吃同住同劳动，这已经打破了纪录片的常规，你是不是也要喷他不专业啊？我看全网至今也只有你在各个平台骂这放屁很差，与大家背道而驰，可能我们都是没鉴赏能力的吧，只有您审美水平高！您够专业！我不会对您人身攻击，因为您够独特！我只想说：您行您上！</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u175009559 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9761449" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9763036" data-cid="9763036" data-user_name="拾叁" data-user_url="https://www.douban.com/people/154747166/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/154747166/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u154747166-3.jpg" alt="拾叁"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/154747166/">拾叁</a>
        <span>2018-08-10 17:45:51</span>
      </div>



      <p class="comment-text">楼主的回复让我意识到我也犯了一个错误，那就是我之前的评论或多或少是在否定你的言论，我在批评你偏激的时候自己却也在偏激，这一点我承认错误，也向你道歉。艺术欣赏就因为欣赏者的不同而具备多样性，所以你正常提出你的想法是正确可取的，所以，我再次表示歉意。但为什么我会在冲动之下向你表示质疑呢，因为我的观点和你完全不一样，位列不同的阵营，难免会有冲突，想必你也能理解。首先是你所提到的影片所出现的旁白做作、刻意煽情和结构混乱等问题，其实可以简单的归咎为导演的不专业，而导演为什么不专业，这一点放屁应该已经给出解释了，导演何苦仅仅只是出于对棒棒行业的缅怀而选择军官转业拍摄了此片，所以首先导演作为一名业余人士，其对艺术的创作肯定有一定局限性，在放屁里一些情节也表现出导演作为个人在性格上的一些缺陷，但这都不影响我们就此否定这部电影，也整整因为这种粗制滥造，才使得放屁有种反向的真实，那种low到底线的真实。而关于摆拍和导演入镜的问题，我有点自己的看法，说与你听，做个讨论。我个人觉得，对于艺术，绝对没有标准可言，自卢米埃尔创造电影以来，从没有哪个人敢拍胸脯说，电影就该这么搞，就连克拉考尔、巴赞这些人的里程碑式的理论也仅仅是电影理论的一个分支而已。而纪录片作为电影的一部分，同样如此。如果我记得没错的话，早期梅里埃拍摄纪录片也有摆拍，而后来的弗拉哈迪这些世纪名导拍摄的纪录片更是表现出一种百家争鸣的态势，具体你可以了解相关影史，我就不赘述了，总的来说就是，既有完全还原真实的纪录片，也有拍摄者直接干涉拍摄的纪录片吗，更有摆拍还原事情原状的纪录片，所以纪录片不仅仅只是现在被广泛认知的单纯实时记录真实事件，所以不管导演是出于拥有丰富的电影理论而有选择的采取这种拍摄方式，还是由于自己的不专业导致的无意识地进行此项操作，但这都不妨碍单论这部电影的所值得被认可的艺术价值很电影拍摄方式。而关于广告植入，其实电影来讲，广告植入很正常，但楼主可能偏执于这是部纪录片，秉持着纪录片必须干净真实的想法，才会如此反感。但我想，或许导演自己都不知道广告植入是个什么东西，版权又是个什么东西，他或许单纯觉得这东西出现在镜头林很正常，他本意或许只是反应客观事实，却弄巧成拙，有了误会而已。对于艺术，我们应该有着一种包容性，这样才能客观理性地去分析去欣赏去感知。就好比《纯洁心灵逐梦演艺圈》这样举世公认的大烂片，你可以恶心它的演员，剧情，拍摄技巧，但你不能否认其表现出来的价值观的正确，只不过表现方式low爆了，我想导演可能只想显露演艺圈的黑暗而已，只不过水平不够，拍的low。所以，我们作为观众，看待电影，首先包容度要足够，才会发现一些我们偏激状态下不能感受到的美！</p>

      <div class="op-lnks">









      </div>

      <div class="group_banned">
        <span class="gact hidden p_u154747166 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9763036" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9772043" data-cid="9772043" data-user_name="青春待出售" data-user_url="https://www.douban.com/people/94177249/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/94177249/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u94177249-2.jpg" alt="青春待出售"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/94177249/">青春待出售</a>
        <span>2018-08-11 13:21:45</span>
      </div>



      <p class="comment-text">第一次回复，楼主是个哈笼包。你先去了解下导演，看看纪录片再来评价。</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u94177249 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9772043" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9775588" data-cid="9775588" data-user_name="思雨" data-user_url="https://www.douban.com/people/182761411/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/182761411/"><img width="48" height="48" src="https://img1.doubanio.com/icon/user_normal.jpg" alt="思雨"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/182761411/">思雨</a>
        <span>2018-08-11 21:21:05</span>
      </div>



      <p class="comment-text">楼主走了，走得很痛苦，火化的时候还诈了尸，一直喊着没有死，最后用铁链绑着烧完的。火很旺，烧得嘎吱嘎吱响，烧了三天三夜。追悼会播放着《今天是个好日子》，家属很坚强，一个哭的都没有，还有一个忍不住笑出了声，那天风很大，运骨灰的路上还翻了车，把骨灰盒摔碎了，刚要捧点儿骨灰，来了一辆洒水车，后来坟头堆起来三米多高，被村支书看见了铲去两米五，撒上生石灰，至今也没长草，好不容易立个碑，结果大冬天的打雷，碑都劈碎了。。。村里的人看不下去了，就把楼主挖了出来，谁也没想到他居然变成了厉鬼。说要到这里来复仇，没办法村民就找来了林正英。林正英用一把桃木剑，插进了楼主心脏，然后祭出九昧真火，准备将他火化，火化的时候眼睛掉出来了，人们说是死不瞑目。火很旺，烧的嗷嗷一直叫，烧了九九八十一天，村民还一起唱《圣诞夜》，村民狠高兴，一个哭的也没有，还有一个忍不住照了张相，林正英想让他入土为安，就给他建了大理石墓。好不容易立了个不锈钢碑。没想到国家试射东风-21导弹偏离弹道，碑都炸碎了，零碎的碑块被踩石场的工人，运去碾成了粉末，粉末糊在修的茅厕墙上，撒尿的人全部把尿射在墙上，不久就会一点一点腐蚀，全部冲进厕所和屎尿一起，一天一头种猪掉进厕所被屎尿给熏死了，楼主的灵魂进入这头猪的身体，一头新生命诞生</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u182761411 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9775588" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9775644" data-cid="9775644" data-user_name="思雨" data-user_url="https://www.douban.com/people/182761411/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/182761411/"><img width="48" height="48" src="https://img1.doubanio.com/icon/user_normal.jpg" alt="思雨"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/182761411/">思雨</a>
        <span>2018-08-11 21:29:20</span>
      </div>



      <p class="comment-text">楼主兄弟我可算找到你了，那年我们一起在深圳的一个充气娃娃厂里做工，我负责装手，你负责装 逼，你装的 逼 滑而蜜，小又香，连厂长都夸你装逼 装的好。后来你就膨胀了，也不好好装 逼了，就被开除了，我以为我再也见不到你了，没想到咱们在这里又见面了[捂脸]</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u182761411 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9775644" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9776279" data-cid="9776279" data-user_name="我非你杯茶yh" data-user_url="https://www.douban.com/people/182692272/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/182692272/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u182692272-1.jpg" alt="我非你杯茶yh"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/182692272/">我非你杯茶yh</a>
        <span>2018-08-11 22:45:45</span>
      </div>



      <p class="comment-text">何苦导演当初的剧场版以两万六的价格给爱奇艺，难以想象吧，看了放屁觉得非常好，所以电影无论都要去支持，你不喜欢就憋在心里，不说没人把你当哑巴</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u182692272 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9776279" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9776872" data-cid="9776872" data-user_name="青春待出售" data-user_url="https://www.douban.com/people/94177249/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/94177249/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u94177249-2.jpg" alt="青春待出售"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/94177249/">青春待出售</a>
        <span>2018-08-11 23:52:37</span>
      </div>



      <p class="comment-text">我看过这个楼主的所有电影评论，感觉是个职业差评师！水军一个，坚定完毕！</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u94177249 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9776872" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9779450" data-cid="9779450" data-user_name="@你的头好大" data-user_url="https://www.douban.com/people/180684781/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/180684781/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u180684781-2.jpg" alt="@你的头好大"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/180684781/">@你的头好大</a>
        <span>2018-08-12 10:30:12</span>
      </div>



      <p class="comment-text">不必和楼主争执什么的，真的没必要。若是审美品味不同还好说，不必深究，但是愚蠢这件事不是区区我等口水可以改变的</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u180684781 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9779450" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9779894" data-cid="9779894" data-user_name="Acid" data-user_url="https://www.douban.com/people/148323786/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9763036">
    <div class="avatar left">
        <a href="https://www.douban.com/people/148323786/"><img width="48" height="48" src="https://img1.doubanio.com/icon/u148323786-8.jpg" alt="Acid"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/148323786/">Acid</a>
        <span>2018-08-12 11:25:23</span>
      </div>



        <div class="reply-quote">
          <span class="short">楼主的回复让我意识到我也犯了一个错误，那就是我之前的评论或多或少是在否定你的言论，我在...</span>
          <span class="all">楼主的回复让我意识到我也犯了一个错误，那就是我之前的评论或多或少是在否定你的言论，我在批评你偏激的时候自己却也在偏激，这一点我承认错误，也向你道歉。艺术欣赏就因为欣赏者的不同而具备多样性，所以你正常提出你的想法是正确可取的，所以，我再次表示歉意。但为什么我会在冲动之下向你表示质疑呢，因为我的观点和你完全不一样，位列不同的阵营，难免会有冲突，想必你也能理解。首先是你所提到的影片所出现的旁白做作、刻意煽情和结构混乱等问题，其实可以简单的归咎为导演的不专业，而导演为什么不专业，这一点放屁应该已经给出解释了，导演何苦仅仅只是出于对棒棒行业的缅怀而选择军官转业拍摄了此片，所以首先导演作为一名业余人士，其对艺术的创作肯定有一定局限性，在放屁里一些情节也表现出导演作为个人在性格上的一些缺陷，但这都不影响我们就此否定这部电影，也整整因为这种粗制滥造，才使得放屁有种反向的真实，那种low到底线的真实。而关于摆拍和导演入镜的问题，我有点自己的看法，说与你听，做个讨论。我个人觉得，对于艺术，绝对没有标准可言，自卢米埃尔创造电影以来，从没有哪个人敢拍胸脯说，电影就该这么搞，就连克拉考尔、巴赞这些人的里程碑式的理论也仅仅是电影理论的一个分支而已。而纪录片作为电影的一部分，同样如此。如果我记得没错的话，早期梅里埃拍摄纪录片也有摆拍，而后来的弗拉哈迪这些世纪名导拍摄的纪录片更是表现出一种百家争鸣的态势，具体你可以了解相关影史，我就不赘述了，总的来说就是，既有完全还原真实的纪录片，也有拍摄者直接干涉拍摄的纪录片吗，更有摆拍还原事情原状的纪录片，所以纪录片不仅仅只是现在被广泛认知的单纯实时记录真实事件，所以不管导演是出于拥有丰富的电影理论而有选择的采取这种拍摄方式，还是由于自己的不专业导致的无意识地进行此项操作，但这都不妨碍单论这部电影的所值得被认可的艺术价值很电影拍摄方式。而关于广告植入，其实电影来讲，广告植入很正常，但楼主可能偏执于这是部纪录片，秉持着纪录片必须干净真实的想法，才会如此反感。但我想，或许导演自己都不知道广告植入是个什么东西，版权又是个什么东西，他或许单纯觉得这东西出现在镜头林很正常，他本意或许只是反应客观事实，却弄巧成拙，有了误会而已。对于艺术，我们应该有着一种包容性，这样才能客观理性地去分析去欣赏去感知。就好比《纯洁心灵逐梦演艺圈》这样举世公认的大烂片，你可以恶心它的演员，剧情，拍摄技巧，但你不能否认其表现出来的价值观的正确，只不过表现方式low爆了，我想导演可能只想显露演艺圈的黑暗而已，只不过水平不够，拍的low。所以，我们作为观众，看待电影，首先包容度要足够，才会发现一些我们偏激状态下不能感受到的美！</span>
          <a href="javascript:;" class="toggle_reply">...</a>
          <span class="pubdate"><a href="https://www.douban.com/people/154747166/">拾叁</a></span>
        </div>


      <p class="comment-text">这个影评写的时候情绪比较激动吧，因为生气。看完这放屁以后我特意和老师讨论了很久，发现我确实是太理想主义了。我的想法就是，对于广告这个问题，如果这个地方很刻意的做了广告，那么会不会整个情节都是存疑的？进而这个放屁的可信度我就不敢判断了。而且培养网红的那个片段，那几个老板和那几个工作人员的讨论非常之生硬虚假，像是刻意搞笑而制造出来的。<br>我觉得是这样，专题纪录片煽情或者有比较多的主观情绪我觉得可以理解。虽然我依然不喜欢。但是这个放屁应该是以真实为主的。我期待看到棒棒的真实生活，真正能震撼我的东西。我觉得他手法上的拙劣影响了这部放屁，或者说是毁掉了它。<br>因为我在看之前是不了解这个导演的，也不是所有人都了解他和他之前的胡说的。所以我抱着很大的期待去看，然后被恶心的彻头彻尾失望透顶。在评价的时候又被一群人劈头盖脸的痛骂，我的客观意见没有得到尊重，无奈之下只能选择写长评这种东西去代表不喜欢的人发一个声。当然我没资格代表别人，这只是一种说辞。但是确实很多人是因为这胡说的拍摄手法产生了厌恶和不喜欢的情绪的。这也是我所说的，既然是上映的电影，应该是以扩大影响力为目的，而不是一小撮看过专题片的观众的狂欢。对于我来说，我觉得导演疯狂的想煽动大家的同情，尊重。反而就适得其反了。要知道一个系列的胡说压缩成电影，应该清楚自己想要表达什么。<br></p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u148323786 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9779894" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9779964" data-cid="9779964" data-user_name="Acid" data-user_url="https://www.douban.com/people/148323786/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9763036">
    <div class="avatar left">
        <a href="https://www.douban.com/people/148323786/"><img width="48" height="48" src="https://img1.doubanio.com/icon/u148323786-8.jpg" alt="Acid"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/148323786/">Acid</a>
        <span>2018-08-12 11:32:02</span>
      </div>



        <div class="reply-quote">
          <span class="short">楼主的回复让我意识到我也犯了一个错误，那就是我之前的评论或多或少是在否定你的言论，我在...</span>
          <span class="all">楼主的回复让我意识到我也犯了一个错误，那就是我之前的评论或多或少是在否定你的言论，我在批评你偏激的时候自己却也在偏激，这一点我承认错误，也向你道歉。艺术欣赏就因为欣赏者的不同而具备多样性，所以你正常提出你的想法是正确可取的，所以，我再次表示歉意。但为什么我会在冲动之下向你表示质疑呢，因为我的观点和你完全不一样，位列不同的阵营，难免会有冲突，想必你也能理解。首先是你所提到的影片所出现的旁白做作、刻意煽情和结构混乱等问题，其实可以简单的归咎为导演的不专业，而导演为什么不专业，这一点胡说应该已经给出解释了，导演何苦仅仅只是出于对棒棒行业的缅怀而选择军官转业拍摄了此片，所以首先导演作为一名业余人士，其对艺术的创作肯定有一定局限性，在胡说里一些情节也表现出导演作为个人在性格上的一些缺陷，但这都不影响我们就此否定这部电影，也整整因为这种粗制滥造，才使得胡说有种反向的真实，那种low到底线的真实。而关于摆拍和导演入镜的问题，我有点自己的看法，说与你听，做个讨论。我个人觉得，对于艺术，绝对没有标准可言，自卢米埃尔创造电影以来，从没有哪个人敢拍胸脯说，电影就该这么搞，就连克拉考尔、巴赞这些人的里程碑式的理论也仅仅是电影理论的一个分支而已。而纪录片作为电影的一部分，同样如此。如果我记得没错的话，早期梅里埃拍摄纪录片也有摆拍，而后来的弗拉哈迪这些世纪名导拍摄的纪录片更是表现出一种百家争鸣的态势，具体你可以了解相关影史，我就不赘述了，总的来说就是，既有完全还原真实的纪录片，也有拍摄者直接干涉拍摄的纪录片吗，更有摆拍还原事情原状的纪录片，所以纪录片不仅仅只是现在被广泛认知的单纯实时记录真实事件，所以不管导演是出于拥有丰富的电影理论而有选择的采取这种拍摄方式，还是由于自己的不专业导致的无意识地进行此项操作，但这都不妨碍单论这部电影的所值得被认可的艺术价值很电影拍摄方式。而关于广告植入，其实电影来讲，广告植入很正常，但楼主可能偏执于这是部纪录片，秉持着纪录片必须干净真实的想法，才会如此反感。但我想，或许导演自己都不知道广告植入是个什么东西，版权又是个什么东西，他或许单纯觉得这东西出现在镜头林很正常，他本意或许只是反应客观事实，却弄巧成拙，有了误会而已。对于艺术，我们应该有着一种包容性，这样才能客观理性地去分析去欣赏去感知。就好比《纯洁心灵逐梦演艺圈》这样举世公认的大烂片，你可以恶心它的演员，剧情，拍摄技巧，但你不能否认其表现出来的价值观的正确，只不过表现方式low爆了，我想导演可能只想显露演艺圈的黑暗而已，只不过水平不够，拍的low。所以，我们作为观众，看待电影，首先包容度要足够，才会发现一些我们偏激状态下不能感受到的美！</span>
          <a href="javascript:;" class="toggle_reply">...</a>
          <span class="pubdate"><a href="https://www.douban.com/people/154747166/">拾叁</a></span>
        </div>


      <p class="comment-text">版权归作者所有，任何形式转载请联系作者。<br>作者：Acid（来自豆瓣）<br>来源：<a href="https://www.douban.com/link2/?url=https%3A%2F%2Fwww.douban.com%2Fdoubanapp%2Fdispatch%3Furi%3D%2Freview%2F9574214%2F">https://www.douban.c<wbr>om/doubanapp/dispatc<wbr>h?uri=/review/957421<wbr>4/</a><br><br>我是真的很厌恶抛开一切去吹捧一部电影，然后疯狂打压不一样声音的人的。所以我非常尊重你，因为你的逻辑上不会有问题，对我也是一个尊重的态度。我还挺感激你能写这么长的评论来跟我讨论的。我是那种忍受不了烂片的人，就是一旦在片子里有了严重的手法上的问题，严重的不合逻辑，严重的演技问题。我就会特别特别不耐烦和愤怒。事实上我也搞不清我为什么会有这么强烈的情绪。你说的这部电影的什么可贵之处，我光是看一个海报其实就已经很明白了，我看了开头就已经了解了。我并不是搞不懂这些内在东西的人。只是这种外壳很难让我去喜欢和尊重。不太想去修改自己影评里的什么措辞。因为这就是我作为一个事先不了解任何东西，去看这部电影的观众的第一观感。我觉得没必要去欲盖弥彰为了少挨骂改什么。被骂我也无所谓，也不在意。</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u148323786 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9779964" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9779998" data-cid="9779998" data-user_name="Acid" data-user_url="https://www.douban.com/people/148323786/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9776872">
    <div class="avatar left">
        <a href="https://www.douban.com/people/148323786/"><img width="48" height="48" src="https://img1.doubanio.com/icon/u148323786-8.jpg" alt="Acid"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/148323786/">Acid</a>
        <span>2018-08-12 11:35:53</span>
      </div>



        <div class="reply-quote">
          <span class="short">我看过这个楼主的所有电影评论，感觉是个职业差评师！水军一个，坚定完毕！</span>
          <span class="all">我看过这个楼主的所有电影评论，感觉是个职业差评师！水军一个，坚定完毕！</span>
          <span class="pubdate"><a href="https://www.douban.com/people/94177249/">青春待出售</a></span>
        </div>


      <p class="comment-text">你很棒啊，能闲到看完了我的所有评价。更帮的是在看完了所有评价以后还能得出我是水军的结论。那我怕是被多个国家联合雇佣了吧？</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u148323786 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9779998" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9781326" data-cid="9781326" data-user_name="缘份、转相守" data-user_url="https://www.douban.com/people/151401326/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/151401326/"><img width="48" height="48" src="https://img1.doubanio.com/icon/u151401326-8.jpg" alt="缘份、转相守"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/151401326/">缘份、转相守</a>
        <span>2018-08-12 14:22:31</span>
      </div>



      <p class="comment-text">楼主你一个人单独刷个差评，在这么多人里面找个存在感吗？明明一个这么好看的纪录片改成的电影，被你踩得一文不值，你说你不是找存在感那是在干嘛？？？？</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u151401326 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9781326" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9786622" data-cid="9786622" data-user_name="主谓语" data-user_url="https://www.douban.com/people/53500463/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/53500463/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u53500463-6.jpg" alt="主谓语"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/53500463/">主谓语</a>
        <span>2018-08-13 08:07:33</span>
      </div>



      <p class="comment-text">首先我还没去看电影  电视剧到看过并认为没有你说的摆拍，混乱和煽情。同样我特别喜欢克制的导演影片，在我看来矛盾的你可以给药神打高分（药神里煽情可以砸屏，就不说里面诸多不自然转变）从说明棒棒电影大可放心去银幕看看。</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u53500463 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9786622" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9786681" data-cid="9786681" data-user_name="寺山青明" data-user_url="https://www.douban.com/people/165805142/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/165805142/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u165805142-1.jpg" alt="寺山青明"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/165805142/">寺山青明</a>
        <span>2018-08-13 08:28:26</span>
      </div>



      <p class="comment-text">“强行安排圆满结局升华到社会主义好”，这是莫大的讽刺。我比较欣赏原版纪录片，但也期待电影能获得票房上的成功。好电影应该是经得起批判的，给个有理有据的差评就要被恶语中伤吗？脆弱的大国公民……</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u165805142 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9786681" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9786981" data-cid="9786981" data-user_name="思雨" data-user_url="https://www.douban.com/people/182761411/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9786681">
    <div class="avatar left">
        <a href="https://www.douban.com/people/182761411/"><img width="48" height="48" src="https://img1.doubanio.com/icon/user_normal.jpg" alt="思雨"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/182761411/">思雨</a>
        <span>2018-08-13 09:26:31</span>
      </div>



        <div class="reply-quote">
          <span class="short">“强行安排圆满结局升华到社会主义好”，这是莫大的讽刺。我比较欣赏原版纪录片，但也期待电...</span>
          <span class="all">“强行安排圆满结局升华到社会主义好”，这是莫大的讽刺。我比较欣赏原版纪录片，但也期待电影能获得票房上的成功。好电影应该是经得起批判的，给个有理有据的差评就要被恶语中伤吗？脆弱的大国公民……</span>
          <a href="javascript:;" class="toggle_reply">...</a>
          <span class="pubdate"><a href="https://www.douban.com/people/165805142/">寺山青明</a></span>
        </div>


      <p class="comment-text">社会主义哪点不好？</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u182761411 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9786981" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9790309" data-cid="9790309" data-user_name="王木木" data-user_url="https://www.douban.com/people/131931537/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/131931537/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u131931537-5.jpg" alt="王木木"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/131931537/">王木木</a>
        <span>2018-08-13 19:26:17</span>
      </div>



      <p class="comment-text">这种就是皮子不舒服想遭决了，相信很多人都觉得楼主说得没有道理，时间在流逝，影视会铭记历史，我重庆人，看到山城棒棒军电影，我会很感谢导演拍出来。楼主该遭决。我先来=_=你妈个楼主长得黑求怪，从小缺钙长大缺爱，买把藤藤菜都要污个口袋，喜欢吃个蛋黄派，把你龟儿弄到菜市场去买，你还逃得飞快，属于心理严重变态，你还活的黑自在，看到就想给你两锅盖</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u131931537 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9790309" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9792957" data-cid="9792957" data-user_name="胡正昱Juan" data-user_url="https://www.douban.com/people/157857956/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/157857956/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u157857956-1.jpg" alt="胡正昱Juan"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/157857956/">胡正昱Juan</a>
        <span>2018-08-14 08:34:55</span>
      </div>



      <p class="comment-text">莫名其妙的优越感</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u157857956 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9792957" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9792978" data-cid="9792978" data-user_name="官人" data-user_url="https://www.douban.com/people/ljy666666/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/ljy666666/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u39215139-43.jpg" alt="官人"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/ljy666666/">官人</a>
        <span>2018-08-14 08:44:19</span>
      </div>



      <p class="comment-text">楼主心理扭曲</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u39215139 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9792978" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9793210" data-cid="9793210" data-user_name="缘份、转相守" data-user_url="https://www.douban.com/people/151401326/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/151401326/"><img width="48" height="48" src="https://img1.doubanio.com/icon/u151401326-8.jpg" alt="缘份、转相守"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/151401326/">缘份、转相守</a>
        <span>2018-08-14 09:34:56</span>
      </div>



      <p class="comment-text">谁来求证一下，这是哪个傻子？整个片的历史都没了解过，就在这瞎评论，发话题。你是告诉大家你是找个存在感还是觉得没事干，在这里面刷存在感？</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u151401326 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9793210" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9793632" data-cid="9793632" data-user_name="Acid" data-user_url="https://www.douban.com/people/148323786/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9786622">
    <div class="avatar left">
        <a href="https://www.douban.com/people/148323786/"><img width="48" height="48" src="https://img1.doubanio.com/icon/u148323786-8.jpg" alt="Acid"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/148323786/">Acid</a>
        <span>2018-08-14 10:46:38</span>
      </div>



        <div class="reply-quote">
          <span class="short">首先我还没去看电影  电视剧到看过并认为没有你说的摆拍，混乱和煽情。同样我特别喜欢克制的...</span>
          <span class="all">首先我还没去看电影  电视剧到看过并认为没有你说的摆拍，混乱和煽情。同样我特别喜欢克制的导演影片，在我看来矛盾的你可以给药神打高分（药神里煽情可以砸屏，就不说里面诸多不自然转变）从说明棒棒电影大可放心去银幕看看。</span>
          <a href="javascript:;" class="toggle_reply">...</a>
          <span class="pubdate"><a href="https://www.douban.com/people/53500463/">主谓语</a></span>
        </div>


      <p class="comment-text">药神我给的分不高，后来考虑到商业性很强很成功还给提了提。反正当时说不好也被疯狂骂了……但跟这个片子比药神至少是及格的。</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u148323786 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9793632" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9793636" data-cid="9793636" data-user_name="Acid" data-user_url="https://www.douban.com/people/148323786/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9786681">
    <div class="avatar left">
        <a href="https://www.douban.com/people/148323786/"><img width="48" height="48" src="https://img1.doubanio.com/icon/u148323786-8.jpg" alt="Acid"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/148323786/">Acid</a>
        <span>2018-08-14 10:47:12</span>
      </div>



        <div class="reply-quote">
          <span class="short">“强行安排圆满结局升华到社会主义好”，这是莫大的讽刺。我比较欣赏原版纪录片，但也期待电...</span>
          <span class="all">“强行安排圆满结局升华到社会主义好”，这是莫大的讽刺。我比较欣赏原版纪录片，但也期待电影能获得票房上的成功。好电影应该是经得起批判的，给个有理有据的差评就要被恶语中伤吗？脆弱的大国公民……</span>
          <a href="javascript:;" class="toggle_reply">...</a>
          <span class="pubdate"><a href="https://www.douban.com/people/165805142/">寺山青明</a></span>
        </div>


      <p class="comment-text">我觉得有讨论挺好的，但是上来就骂人有点诡异了。</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u148323786 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9793636" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9793639" data-cid="9793639" data-user_name="Acid" data-user_url="https://www.douban.com/people/148323786/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9790309">
    <div class="avatar left">
        <a href="https://www.douban.com/people/148323786/"><img width="48" height="48" src="https://img1.doubanio.com/icon/u148323786-8.jpg" alt="Acid"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/148323786/">Acid</a>
        <span>2018-08-14 10:47:42</span>
      </div>



        <div class="reply-quote">
          <span class="short">这种就是皮子不舒服想遭决了，相信很多人都觉得楼主说得没有道理，时间在流逝，影视会铭记历...</span>
          <span class="all">这种就是皮子不舒服想遭决了，相信很多人都觉得楼主说得没有道理，时间在流逝，影视会铭记历史，我重庆人，看到山城棒棒军电影，我会很感谢导演拍出来。楼主该遭决。我先来=_=你妈个楼主长得黑求怪，从小缺钙长大缺爱，买把藤藤菜都要污个口袋，喜欢吃个蛋黄派，把你龟儿弄到菜市场去买，你还逃得飞快，属于心理严重变态，你还活的黑自在，看到就想给你两锅盖</span>
          <a href="javascript:;" class="toggle_reply">...</a>
          <span class="pubdate"><a href="https://www.douban.com/people/131931537/">王木木</a></span>
        </div>


      <p class="comment-text">谢谢</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u148323786 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9793639" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9793642" data-cid="9793642" data-user_name="Acid" data-user_url="https://www.douban.com/people/148323786/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9781326">
    <div class="avatar left">
        <a href="https://www.douban.com/people/148323786/"><img width="48" height="48" src="https://img1.doubanio.com/icon/u148323786-8.jpg" alt="Acid"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/148323786/">Acid</a>
        <span>2018-08-14 10:47:59</span>
      </div>



        <div class="reply-quote">
          <span class="short">楼主你一个人单独刷个差评，在这么多人里面找个存在感吗？明明一个这么好看的纪录片改成的电...</span>
          <span class="all">楼主你一个人单独刷个差评，在这么多人里面找个存在感吗？明明一个这么好看的纪录片改成的电影，被你踩得一文不值，你说你不是找存在感那是在干嘛？？？？</span>
          <a href="javascript:;" class="toggle_reply">...</a>
          <span class="pubdate"><a href="https://www.douban.com/people/151401326/">缘份、转相守</a></span>
        </div>


      <p class="comment-text">对，我太缺爱了。</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u148323786 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9793642" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9793770" data-cid="9793770" data-user_name="石头之魂" data-user_url="https://www.douban.com/people/141667608/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/141667608/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u141667608-3.jpg" alt="石头之魂"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/141667608/">石头之魂</a>
        <span>2018-08-14 11:09:51</span>
      </div>



      <p class="comment-text">其实楼主在探讨他不喜欢影版的原因，而大家再拿剧版的好口碑加上电影本身的社会关怀在和楼主争论！表达自己的不喜欢，并且有理有据，没什么不妥，反而是大家喷的太感性了，其实从某种意义上来说，骂出来的人，和鼓励的人都有一个共同点，就是希望他越来越好，因为不在乎的话，就不会讨论了！所以，无论技术还是感情，希望他更好吧，金无足赤，精益求精！</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u141667608 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9793770" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9794191" data-cid="9794191" data-user_name="大海里的针" data-user_url="https://www.douban.com/people/65569388/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/65569388/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u65569388-2.jpg" alt="大海里的针"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/65569388/">大海里的针</a>  (路人视角，不吹不黑)
        <span>2018-08-14 12:38:24</span>
      </div>



      <p class="comment-text">说纪录片必须克制的，怕是没听说过《意志的胜利》，煽动性很强，却是影史经典</p>

      <div class="op-lnks">









      </div>

      <div class="group_banned">
        <span class="gact hidden p_u65569388 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9794191" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9794335" data-cid="9794335" data-user_name="Soldier" data-user_url="https://www.douban.com/people/164086783/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/164086783/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u164086783-1.jpg" alt="Soldier"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/164086783/">Soldier</a>
        <span>2018-08-14 13:06:52</span>
      </div>



      <p class="comment-text">还写影评的时候比较激动，还生气！你有什么权利资格生气？世界上就是有你这么一号觉得你自己全懂完了，然后肆无忌惮的满嘴喷粪，其实就一13点！先做人后做事，最后送你一句包皮龙！</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u164086783 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9794335" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9794836" data-cid="9794836" data-user_name="李载文Zevin" data-user_url="https://www.douban.com/people/70947086/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9759438">
    <div class="avatar left">
        <a href="https://www.douban.com/people/70947086/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u70947086-4.jpg" alt="李载文Zevin"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/70947086/">李载文Zevin</a>
        <span>2018-08-14 14:36:35</span>
      </div>



        <div class="reply-quote">
          <span class="short">1.高评分是剧集版
2.高评分不代表绝对优秀
3.纪录片是有底线的
4.自己没有鉴赏能力就不要胡乱...</span>
          <span class="all">1.高评分是剧集版
2.高评分不代表绝对优秀
3.纪录片是有底线的
4.自己没有鉴赏能力就不要胡乱反问我。这种你从哪儿看出来xxx的话很没营养，就好像你从哪儿看出1+1=2一样。
5.你的观后感是你自己的想法，我只是说我为什么不喜欢，碍着你喜欢什么事了？这么激动有什么意义？
6.我有一说一，没有一点扒瞎，你管这叫恶意给低分。所以只有给你觉得应该高分的电影高分，给你觉得应该低分的电影低分才叫不恶意是吗？你是标尺？</span>
          <a href="javascript:;" class="toggle_reply">...</a>
          <span class="pubdate"><a href="https://www.douban.com/people/148323786/">Acid</a></span>
        </div>


      <p class="comment-text">1.电影版上映后一样会高评分<br>2.确实不代表绝对优秀，但是低评分一定代表不优秀，什么电影是打1星的？《逐梦演艺圈》和《爱情公寓》，你给《最后的棒棒》打1星难道不叫恶意差评？<br>3.你以为纪录片就不能包含导演的引导吗，只要是人做的事都包含主观意愿，纪录片也是电影艺术的一种，镜头的运用、素材的采用，都是可以导演选择的事，摆拍怎么了？哪一部纪录片全程都没有摆拍，重要的不是形式是内容<br>4. 你怀疑那些故事的真实性？我告诉你，我是重庆人，以前我身边就有很多棒棒，我了解重庆棒棒的生活，所以我知道《最后的棒棒》里的那些棒棒经历的事都是真实的，你质疑真实性才是主观臆测，你了解过棒棒的真实生活吗？<br>4.最后，我也大概去看了一下你对其他电影的评价，我发现普遍偏低，这说明什么呢？不过说明你是一个眼光挑剔吝于欣赏心胸狭隘自命不凡的人罢了</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u70947086 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9794836" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9794841" data-cid="9794841" data-user_name="OLD BOY" data-user_url="https://www.douban.com/people/182940752/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/182940752/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u182940752-1.jpg" alt="OLD BOY"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/182940752/">OLD BOY</a>
        <span>2018-08-14 14:37:33</span>
      </div>



      <p class="comment-text">他是让你了解棒棒 因为现在很多年轻人都不知道棒棒是什么 是干嘛的 并不是消费棒棒 如果没有最后的棒棒这个视频 那以后只能从网上查了 根本了解不到棒棒在现代社会里最后的挣扎 经历的辛酸苦辣 你这样说真是误导大家</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u182940752 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9794841" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9794928" data-cid="9794928" data-user_name="johly" data-user_url="https://www.douban.com/people/156644355/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/156644355/"><img width="48" height="48" src="https://img1.doubanio.com/icon/user_normal.jpg" alt="johly"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/156644355/">johly</a>
        <span>2018-08-14 14:58:34</span>
      </div>



      <p class="comment-text">据说这个是电视剧压缩版加几年后的现状，剧集版很感人，不敢说全程无摆拍，剧集版真实记录实拍的占了99%，不知道是不是拿放大镜出来找的摆拍！</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u156644355 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9794928" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9795273" data-cid="9795273" data-user_name="lsvexy" data-user_url="https://www.douban.com/people/127527152/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9761266">
    <div class="avatar left">
        <a href="https://www.douban.com/people/127527152/"><img width="48" height="48" src="https://img1.doubanio.com/icon/user_normal.jpg" alt="lsvexy"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/127527152/">lsvexy</a>
        <span>2018-08-14 16:26:43</span>
      </div>



        <div class="reply-quote">
          <span class="short">辩不明白就人身攻击，牛逼，服气。我恶意评论，我恶毒。谢谢您。</span>
          <span class="all">辩不明白就人身攻击，牛逼，服气。我恶意评论，我恶毒。谢谢您。</span>
          <span class="pubdate"><a href="https://www.douban.com/people/148323786/">Acid</a></span>
        </div>


      <p class="comment-text">攻击的就是你，你妈把你养这么大不容易，快回去给你妈推轮椅吧脑残东西。</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u127527152 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9795273" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9795808" data-cid="9795808" data-user_name="q" data-user_url="https://www.douban.com/people/179154863/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/179154863/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u179154863-1.jpg" alt="q"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/179154863/">q</a>
        <span>2018-08-14 18:18:38</span>
      </div>



      <p class="comment-text">版权归作者所有，任何形式转载请联系作者。<br>作者：Acid（来自豆瓣）<br>来源：<a href="https://www.douban.com/link2/?url=https%3A%2F%2Fwww.douban.com%2Fdoubanapp%2Fdispatch%3Furi%3D%2Freview%2F9574214%2F">https://www.douban.c<wbr>om/doubanapp/dispatc<wbr>h?uri=/review/957421<wbr>4/</a><br><br>麻烦你先看一下剧集版，其次这是电影！电影！摆拍？这位兄弟，怕你是搞笑。而且 你知道什么事纪录片么？目前都没有确定的纪录片定义吧</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u179154863 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9795808" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9796993" data-cid="9796993" data-user_name="瓢儿糕" data-user_url="https://www.douban.com/people/xiaobowen/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/xiaobowen/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u49363701-25.jpg" alt="瓢儿糕"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/xiaobowen/">瓢儿糕</a>  (月寒日暖，来煎人寿。)
        <span>2018-08-14 22:55:19</span>
      </div>



      <p class="comment-text">能够理解楼主为何会反感电影版，因为它不符合楼主的布尔乔亚审美品位，但架不住劳动人民说喜欢。</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u49363701 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9796993" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9797285" data-cid="9797285" data-user_name="想得美" data-user_url="https://www.douban.com/people/170952952/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/170952952/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u170952952-3.jpg" alt="想得美"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/170952952/">想得美</a>
        <span>2018-08-14 23:39:25</span>
      </div>



      <p class="comment-text">烂烂烂烂尼玛个老母猪，老母猪是你屋姑姑，你姑姑脑壳有点秃，呛尼玛颗夜明珠</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u170952952 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9797285" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9798017" data-cid="9798017" data-user_name="谁的爱温暖了我" data-user_url="https://www.douban.com/people/131784501/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/131784501/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u131784501-1.jpg" alt="谁的爱温暖了我"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/131784501/">谁的爱温暖了我</a>
        <span>2018-08-15 06:22:27</span>
      </div>



      <p class="comment-text">你不喜欢电影版  但是你也得一尊重  你只是在刻意发泄你的不喜欢而已 搞的自己很牛逼一样，就你一个人会影评吗？ 什么样的是烂片？  在你眼中就是你不喜欢的就是烂片  什么可以摆拍  故意煽情？ 还好意思说宁可花八小时去看一部不带任何色彩的作品，也不愿意看故意煽情的片子 你是在搞笑吗？</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u131784501 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9798017" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9798695" data-cid="9798695" data-user_name="singer33" data-user_url="https://www.douban.com/people/singer33/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/singer33/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u33827526-5.jpg" alt="singer33"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/singer33/">singer33</a>  (在希望的田野上慢跑)
        <span>2018-08-15 10:41:56</span>
      </div>



      <p class="comment-text">因为你是傻逼</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u33827526 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9798695" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9799024" data-cid="9799024" data-user_name="moby1999" data-user_url="https://www.douban.com/people/115916349/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/115916349/"><img width="48" height="48" src="https://img1.doubanio.com/icon/user_normal.jpg" alt="moby1999"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/115916349/">moby1999</a>
        <span>2018-08-15 11:46:47</span>
      </div>



      <p class="comment-text">只想说，剧集版看得我无声泪流</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u115916349 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9799024" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9799486" data-cid="9799486" data-user_name="乌拉拉" data-user_url="https://www.douban.com/people/61041468/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/61041468/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u61041468-5.jpg" alt="乌拉拉"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/61041468/">乌拉拉</a>
        <span>2018-08-15 13:31:34</span>
      </div>



      <p class="comment-text">建议楼主去看下原版纪录片</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u61041468 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9799486" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9800703" data-cid="9800703" data-user_name="青春待出售" data-user_url="https://www.douban.com/people/94177249/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9779998">
    <div class="avatar left">
        <a href="https://www.douban.com/people/94177249/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u94177249-2.jpg" alt="青春待出售"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/94177249/">青春待出售</a>
        <span>2018-08-15 18:37:18</span>
      </div>



        <div class="reply-quote">
          <span class="short">你很棒啊，能闲到看完了我的所有评价。更帮的是在看完了所有评价以后还能得出我是水军的结论...</span>
          <span class="all">你很棒啊，能闲到看完了我的所有评价。更帮的是在看完了所有评价以后还能得出我是水军的结论。那我怕是被多个国家联合雇佣了吧？</span>
          <a href="javascript:;" class="toggle_reply">...</a>
          <span class="pubdate"><a href="https://www.douban.com/people/148323786/">Acid</a></span>
        </div>


      <p class="comment-text">不想回复你！不值得！</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u94177249 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9800703" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9800898" data-cid="9800898" data-user_name="可爱萌萌望蓝天" data-user_url="https://www.douban.com/people/121918691/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9756042">
    <div class="avatar left">
        <a href="https://www.douban.com/people/121918691/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u121918691-5.jpg" alt="可爱萌萌望蓝天"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/121918691/">可爱萌萌望蓝天</a>
        <span>2018-08-15 19:33:13</span>
      </div>



        <div class="reply-quote">
          <span class="short">还有，你说何苦不尊重棒棒，消费棒棒，你是怎么说出口的？他为了这个行业为了这些人做过多少...</span>
          <span class="all">还有，你说何苦不尊重棒棒，消费棒棒，你是怎么说出口的？他为了这个行业为了这些人做过多少事情，你看到了吗？如果没有他，这几位棒棒师傅的老年生活会得到重视吗？何苦过年拿自己的积蓄为几百位棒棒师傅团年，送他们棉大衣，默默做了好几年，你知道吗？你到底有何居心？如果他做的不好，会有那么高的评分么？如果片子不好看，会得到那么多人的认可么？</span>
          <a href="javascript:;" class="toggle_reply">...</a>
          <span class="pubdate"><a href="https://www.douban.com/people/175009559/">立春</a></span>
        </div>


      <p class="comment-text">是的呀，小时候，到处都有棒棒，随着时代的变化，现在真的没怎么看到了，小时候看《山城棒棒军》觉得特别好看，从里面走出来的演员也有现在在大银幕里混的了，但是棒棒真的值得纪念</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u121918691 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9800898" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9801450" data-cid="9801450" data-user_name="辉__" data-user_url="https://www.douban.com/people/103390292/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/103390292/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u103390292-1.jpg" alt="辉__"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/103390292/">辉__</a>
        <span>2018-08-15 21:53:27</span>
      </div>



      <p class="comment-text">我觉得楼主和我想的差不多，就是言辞比较严重，作品结尾和植入确实是败笔，但还不至于一星哈</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u103390292 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9801450" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9801607" data-cid="9801607" data-user_name="滑之多恶好" data-user_url="https://www.douban.com/people/163250141/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/163250141/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u163250141-6.jpg" alt="滑之多恶好"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/163250141/">滑之多恶好</a>
        <span>2018-08-15 22:29:48</span>
      </div>



      <p class="comment-text">是不是重庆人？看过山城棒棒军吗？</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u163250141 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9801607" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9801996" data-cid="9801996" data-user_name="遥远" data-user_url="https://www.douban.com/people/3193575/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9763036">
    <div class="avatar left">
        <a href="https://www.douban.com/people/3193575/"><img width="48" height="48" src="https://img1.doubanio.com/icon/user_normal.jpg" alt="遥远"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/3193575/">遥远</a>
        <span>2018-08-15 23:44:19</span>
      </div>



        <div class="reply-quote">
          <span class="short">楼主的回复让我意识到我也犯了一个错误，那就是我之前的评论或多或少是在否定你的言论，我在...</span>
          <span class="all">楼主的回复让我意识到我也犯了一个错误，那就是我之前的评论或多或少是在否定你的言论，我在批评你偏激的时候自己却也在偏激，这一点我承认错误，也向你道歉。艺术欣赏就因为欣赏者的不同而具备多样性，所以你正常提出你的想法是正确可取的，所以，我再次表示歉意。但为什么我会在冲动之下向你表示质疑呢，因为我的观点和你完全不一样，位列不同的阵营，难免会有冲突，想必你也能理解。首先是你所提到的影片所出现的旁白做作、刻意煽情和结构混乱等问题，其实可以简单的归咎为导演的不专业，而导演为什么不专业，这一点片子应该已经给出解释了，导演何苦仅仅只是出于对棒棒行业的缅怀而选择军官转业拍摄了此片，所以首先导演作为一名业余人士，其对艺术的创作肯定有一定局限性，在片子里一些情节也表现出导演作为个人在性格上的一些缺陷，但这都不影响我们就此否定这部电影，也整整因为这种粗制滥造，才使得片子有种反向的真实，那种low到底线的真实。而关于摆拍和导演入镜的问题，我有点自己的看法，说与你听，做个讨论。我个人觉得，对于艺术，绝对没有标准可言，自卢米埃尔创造电影以来，从没有哪个人敢拍胸脯说，电影就该这么搞，就连克拉考尔、巴赞这些人的里程碑式的理论也仅仅是电影理论的一个分支而已。而纪录片作为电影的一部分，同样如此。如果我记得没错的话，早期梅里埃拍摄纪录片也有摆拍，而后来的弗拉哈迪这些世纪名导拍摄的纪录片更是表现出一种百家争鸣的态势，具体你可以了解相关影史，我就不赘述了，总的来说就是，既有完全还原真实的纪录片，也有拍摄者直接干涉拍摄的纪录片吗，更有摆拍还原事情原状的纪录片，所以纪录片不仅仅只是现在被广泛认知的单纯实时记录真实事件，所以不管导演是出于拥有丰富的电影理论而有选择的采取这种拍摄方式，还是由于自己的不专业导致的无意识地进行此项操作，但这都不妨碍单论这部电影的所值得被认可的艺术价值很电影拍摄方式。而关于广告植入，其实电影来讲，广告植入很正常，但楼主可能偏执于这是部纪录片，秉持着纪录片必须干净真实的想法，才会如此反感。但我想，或许导演自己都不知道广告植入是个什么东西，版权又是个什么东西，他或许单纯觉得这东西出现在镜头林很正常，他本意或许只是反应客观事实，却弄巧成拙，有了误会而已。对于艺术，我们应该有着一种包容性，这样才能客观理性地去分析去欣赏去感知。就好比《纯洁心灵逐梦演艺圈》这样举世公认的大烂片，你可以恶心它的演员，剧情，拍摄技巧，但你不能否认其表现出来的价值观的正确，只不过表现方式low爆了，我想导演可能只想显露演艺圈的黑暗而已，只不过水平不够，拍的low。所以，我们作为观众，看待电影，首先包容度要足够，才会发现一些我们偏激状态下不能感受到的美！</span>
          <a href="javascript:;" class="toggle_reply">...</a>
          <span class="pubdate"><a href="https://www.douban.com/people/154747166/">拾叁</a></span>
        </div>


      <p class="comment-text">给你鼓掌👏👏👏</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u3193575 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9801996" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9803181" data-cid="9803181" data-user_name="斑马" data-user_url="https://www.douban.com/people/144238862/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/144238862/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u144238862-5.jpg" alt="斑马"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/144238862/">斑马</a>
        <span>2018-08-16 09:33:15</span>
      </div>



      <p class="comment-text">你他妈才是真的放屁。</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u144238862 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9803181" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9803184" data-cid="9803184" data-user_name="斑马" data-user_url="https://www.douban.com/people/144238862/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/144238862/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u144238862-5.jpg" alt="斑马"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/144238862/">斑马</a>
        <span>2018-08-16 09:34:02</span>
      </div>



      <p class="comment-text">你有个屁的艺术鉴赏能力，垃圾</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u144238862 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9803184" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9803271" data-cid="9803271" data-user_name="木家卫" data-user_url="https://www.douban.com/people/84184278/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/84184278/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u84184278-4.jpg" alt="木家卫"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/84184278/">木家卫</a>
        <span>2018-08-16 09:58:00</span>
      </div>



      <p class="comment-text">楼主所理解的纪录片概念太狭隘了，从梅里爱排演的新闻片，到弗拉哈迪的《北方的纳努克》，摆拍还原是纪录片的一部分。其他的内容还没看过电影，不敢评价，就这一部分而言，几乎没有纪录片是完全的事实记载，哪怕新闻片，编导的主观因素也会影响剪辑，毕竟电影是人的艺术，要体现人的思想</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u84184278 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9803271" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9803490" data-cid="9803490" data-user_name="帅帅不懂爱" data-user_url="https://www.douban.com/people/72129082/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9794836">
    <div class="avatar left">
        <a href="https://www.douban.com/people/72129082/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u72129082-2.jpg" alt="帅帅不懂爱"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/72129082/">帅帅不懂爱</a>  (设计狮)
        <span>2018-08-16 10:53:55</span>
      </div>



        <div class="reply-quote">
          <span class="short">1.电影版上映后一样会高评分
2.确实不代表绝对优秀，但是低评分一定代表不优秀，什么电影是打...</span>
          <span class="all">1.电影版上映后一样会高评分
2.确实不代表绝对优秀，但是低评分一定代表不优秀，什么电影是打1星的？《逐梦演艺圈》和《爱情公寓》，你给《最后的棒棒》打1星难道不叫恶意差评？
3.你以为纪录片就不能包含导演的引导吗，只要是人做的事都包含主观意愿，纪录片也是电影艺术的一种，镜头的运用、素材的采用，都是可以导演选择的事，摆拍怎么了？哪一部纪录片全程都没有摆拍，重要的不是形式是内容
4. 你怀疑那些故事的真实性？我告诉你，我是重庆人，以前我身边就有很多棒棒，我了解重庆棒棒的生活，所以我知道《最后的棒棒》里的那些棒棒经历的事都是真实的，你质疑真实性才是主观臆测，你了解过棒棒的真实生活吗？
4.最后，我也大概去看了一下你对其他电影的评价，我发现普遍偏低，这说明什么呢？不过说明你是一个眼光挑剔吝于欣赏心胸狭隘自命不凡的人罢了</span>
          <a href="javascript:;" class="toggle_reply">...</a>
          <span class="pubdate"><a href="https://www.douban.com/people/70947086/">李载文Zevin</a></span>
        </div>


      <p class="comment-text">最后一句点题了</p>

      <div class="op-lnks">









      </div>

      <div class="group_banned">
        <span class="gact hidden p_u72129082 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9803490" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9803645" data-cid="9803645" data-user_name="段润" data-user_url="https://www.douban.com/people/179853490/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9763036">
    <div class="avatar left">
        <a href="https://www.douban.com/people/179853490/"><img width="48" height="48" src="https://img1.doubanio.com/icon/user_normal.jpg" alt="段润"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/179853490/">段润</a>
        <span>2018-08-16 11:22:55</span>
      </div>



        <div class="reply-quote">
          <span class="short">楼主的回复让我意识到我也犯了一个错误，那就是我之前的评论或多或少是在否定你的言论，我在...</span>
          <span class="all">楼主的回复让我意识到我也犯了一个错误，那就是我之前的评论或多或少是在否定你的言论，我在批评你偏激的时候自己却也在偏激，这一点我承认错误，也向你道歉。艺术欣赏就因为欣赏者的不同而具备多样性，所以你正常提出你的想法是正确可取的，所以，我再次表示歉意。但为什么我会在冲动之下向你表示质疑呢，因为我的观点和你完全不一样，位列不同的阵营，难免会有冲突，想必你也能理解。首先是你所提到的影片所出现的旁白做作、刻意煽情和结构混乱等问题，其实可以简单的归咎为导演的不专业，而导演为什么不专业，这一点片子应该已经给出解释了，导演何苦仅仅只是出于对棒棒行业的缅怀而选择军官转业拍摄了此片，所以首先导演作为一名业余人士，其对艺术的创作肯定有一定局限性，在片子里一些情节也表现出导演作为个人在性格上的一些缺陷，但这都不影响我们就此否定这部电影，也整整因为这种粗制滥造，才使得片子有种反向的真实，那种low到底线的真实。而关于摆拍和导演入镜的问题，我有点自己的看法，说与你听，做个讨论。我个人觉得，对于艺术，绝对没有标准可言，自卢米埃尔创造电影以来，从没有哪个人敢拍胸脯说，电影就该这么搞，就连克拉考尔、巴赞这些人的里程碑式的理论也仅仅是电影理论的一个分支而已。而纪录片作为电影的一部分，同样如此。如果我记得没错的话，早期梅里埃拍摄纪录片也有摆拍，而后来的弗拉哈迪这些世纪名导拍摄的纪录片更是表现出一种百家争鸣的态势，具体你可以了解相关影史，我就不赘述了，总的来说就是，既有完全还原真实的纪录片，也有拍摄者直接干涉拍摄的纪录片吗，更有摆拍还原事情原状的纪录片，所以纪录片不仅仅只是现在被广泛认知的单纯实时记录真实事件，所以不管导演是出于拥有丰富的电影理论而有选择的采取这种拍摄方式，还是由于自己的不专业导致的无意识地进行此项操作，但这都不妨碍单论这部电影的所值得被认可的艺术价值很电影拍摄方式。而关于广告植入，其实电影来讲，广告植入很正常，但楼主可能偏执于这是部纪录片，秉持着纪录片必须干净真实的想法，才会如此反感。但我想，或许导演自己都不知道广告植入是个什么东西，版权又是个什么东西，他或许单纯觉得这东西出现在镜头林很正常，他本意或许只是反应客观事实，却弄巧成拙，有了误会而已。对于艺术，我们应该有着一种包容性，这样才能客观理性地去分析去欣赏去感知。就好比《纯洁心灵逐梦演艺圈》这样举世公认的大烂片，你可以恶心它的演员，剧情，拍摄技巧，但你不能否认其表现出来的价值观的正确，只不过表现方式low爆了，我想导演可能只想显露演艺圈的黑暗而已，只不过水平不够，拍的low。所以，我们作为观众，看待电影，首先包容度要足够，才会发现一些我们偏激状态下不能感受到的美！</span>
          <a href="javascript:;" class="toggle_reply">...</a>
          <span class="pubdate"><a href="https://www.douban.com/people/154747166/">拾叁</a></span>
        </div>


      <p class="comment-text">您太会自我合理化了</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u179853490 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9803645" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9803689" data-cid="9803689" data-user_name="拾叁" data-user_url="https://www.douban.com/people/154747166/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9803645">
    <div class="avatar left">
        <a href="https://www.douban.com/people/154747166/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u154747166-3.jpg" alt="拾叁"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/154747166/">拾叁</a>
        <span>2018-08-16 11:30:20</span>
      </div>



        <div class="reply-quote">
          <span class="short">您太会自我合理化了</span>
          <span class="all">您太会自我合理化了</span>
          <span class="pubdate"><a href="https://www.douban.com/people/179853490/">段润</a></span>
        </div>


      <p class="comment-text">您自我组词能力也不弱😁</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u154747166 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9803689" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9803726" data-cid="9803726" data-user_name="段润" data-user_url="https://www.douban.com/people/179853490/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9786681">
    <div class="avatar left">
        <a href="https://www.douban.com/people/179853490/"><img width="48" height="48" src="https://img1.doubanio.com/icon/user_normal.jpg" alt="段润"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/179853490/">段润</a>
        <span>2018-08-16 11:38:07</span>
      </div>



        <div class="reply-quote">
          <span class="short">“强行安排圆满结局升华到社会主义好”，这是莫大的讽刺。我比较欣赏原版纪录片，但也期待电...</span>
          <span class="all">“强行安排圆满结局升华到社会主义好”，这是莫大的讽刺。我比较欣赏原版纪录片，但也期待电影能获得票房上的成功。好电影应该是经得起批判的，给个有理有据的差评就要被恶语中伤吗？脆弱的大国公民……</span>
          <a href="javascript:;" class="toggle_reply">...</a>
          <span class="pubdate"><a href="https://www.douban.com/people/165805142/">寺山青明</a></span>
        </div>


      <p class="comment-text">所言极是</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u179853490 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9803726" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9803729" data-cid="9803729" data-user_name="段润" data-user_url="https://www.douban.com/people/179853490/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9798017">
    <div class="avatar left">
        <a href="https://www.douban.com/people/179853490/"><img width="48" height="48" src="https://img1.doubanio.com/icon/user_normal.jpg" alt="段润"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/179853490/">段润</a>
        <span>2018-08-16 11:39:00</span>
      </div>



        <div class="reply-quote">
          <span class="short">你不喜欢电影版  但是你也得一尊重  你只是在刻意发泄你的不喜欢而已 搞的自己很牛逼一样，就...</span>
          <span class="all">你不喜欢电影版  但是你也得一尊重  你只是在刻意发泄你的不喜欢而已 搞的自己很牛逼一样，就你一个人会影评吗？ 什么样的是烂片？  在你眼中就是你不喜欢的就是烂片  什么可以摆拍  故意煽情？ 还好意思说宁可花八小时去看一部不带任何色彩的作品，也不愿意看故意煽情的片子 你是在搞笑吗？</span>
          <a href="javascript:;" class="toggle_reply">...</a>
          <span class="pubdate"><a href="https://www.douban.com/people/131784501/">谁的爱温暖了我</a></span>
        </div>


      <p class="comment-text">是的，我觉得你挺搞笑的</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u179853490 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9803729" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9803741" data-cid="9803741" data-user_name="段润" data-user_url="https://www.douban.com/people/179853490/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9803271">
    <div class="avatar left">
        <a href="https://www.douban.com/people/179853490/"><img width="48" height="48" src="https://img1.doubanio.com/icon/user_normal.jpg" alt="段润"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/179853490/">段润</a>
        <span>2018-08-16 11:41:14</span>
      </div>



        <div class="reply-quote">
          <span class="short">楼主所理解的纪录片概念太狭隘了，从梅里爱排演的新闻片，到弗拉哈迪的《北方的纳努克》，摆...</span>
          <span class="all">楼主所理解的纪录片概念太狭隘了，从梅里爱排演的新闻片，到弗拉哈迪的《北方的纳努克》，摆拍还原是纪录片的一部分。其他的内容还没看过电影，不敢评价，就这一部分而言，几乎没有纪录片是完全的事实记载，哪怕新闻片，编导的主观因素也会影响剪辑，毕竟电影是人的艺术，要体现人的思想</span>
          <a href="javascript:;" class="toggle_reply">...</a>
          <span class="pubdate"><a href="https://www.douban.com/people/84184278/">木家卫</a></span>
        </div>


      <p class="comment-text">我想楼主本质讨厌的是导演主观上某些强加的东西</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u179853490 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9803741" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9803766" data-cid="9803766" data-user_name="木家卫" data-user_url="https://www.douban.com/people/84184278/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9803741">
    <div class="avatar left">
        <a href="https://www.douban.com/people/84184278/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u84184278-4.jpg" alt="木家卫"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/84184278/">木家卫</a>
        <span>2018-08-16 11:47:07</span>
      </div>



        <div class="reply-quote">
          <span class="short">我想楼主本质讨厌的是导演主观上某些强加的东西</span>
          <span class="all">我想楼主本质讨厌的是导演主观上某些强加的东西</span>
          <span class="pubdate"><a href="https://www.douban.com/people/179853490/">段润</a></span>
        </div>


      <p class="comment-text">哦哦，可能吧，文无第一，尊重别人的想法和审美权利，所以只能稍微解释一下纪录片摆拍的问题。</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u84184278 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9803766" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9803835" data-cid="9803835" data-user_name="段润" data-user_url="https://www.douban.com/people/179853490/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9803766">
    <div class="avatar left">
        <a href="https://www.douban.com/people/179853490/"><img width="48" height="48" src="https://img1.doubanio.com/icon/user_normal.jpg" alt="段润"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/179853490/">段润</a>
        <span>2018-08-16 12:07:01</span>
      </div>



        <div class="reply-quote">
          <span class="short">哦哦，可能吧，文无第一，尊重别人的想法和审美权利，所以只能稍微解释一下纪录片摆拍的问题。</span>
          <span class="all">哦哦，可能吧，文无第一，尊重别人的想法和审美权利，所以只能稍微解释一下纪录片摆拍的问题。</span>
          <span class="pubdate"><a href="https://www.douban.com/people/84184278/">木家卫</a></span>
        </div>


      <p class="comment-text">影评本是立足于电影本身，再谈个人想法，观点，感受，楼主只是正常影评，也很有见解。大家太把自己的意愿强加于他的影评身上。</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u179853490 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9803835" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9803872" data-cid="9803872" data-user_name="立春" data-user_url="https://www.douban.com/people/175009559/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9800898">
    <div class="avatar left">
        <a href="https://www.douban.com/people/175009559/"><img width="48" height="48" src="https://img1.doubanio.com/icon/user_normal.jpg" alt="立春"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/175009559/">立春</a>
        <span>2018-08-16 12:15:47</span>
      </div>



        <div class="reply-quote">
          <span class="short">是的呀，小时候，到处都有棒棒，随着时代的变化，现在真的没怎么看到了，小时候看《山城棒棒...</span>
          <span class="all">是的呀，小时候，到处都有棒棒，随着时代的变化，现在真的没怎么看到了，小时候看《山城棒棒军》觉得特别好看，从里面走出来的演员也有现在在大银幕里混的了，但是棒棒真的值得纪念</span>
          <a href="javascript:;" class="toggle_reply">...</a>
          <span class="pubdate"><a href="https://www.douban.com/people/121918691/">可爱萌萌望蓝天</a></span>
        </div>


      <p class="comment-text">嗯嗯，他们为重庆的建设发展做出了不可磨灭的贡献</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u175009559 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9803872" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9803893" data-cid="9803893" data-user_name="木家卫" data-user_url="https://www.douban.com/people/84184278/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9803835">
    <div class="avatar left">
        <a href="https://www.douban.com/people/84184278/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u84184278-4.jpg" alt="木家卫"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/84184278/">木家卫</a>
        <span>2018-08-16 12:21:45</span>
      </div>



        <div class="reply-quote">
          <span class="short">影评本是立足于电影本身，再谈个人想法，观点，感受，楼主只是正常影评，也很有见解。大家太...</span>
          <span class="all">影评本是立足于电影本身，再谈个人想法，观点，感受，楼主只是正常影评，也很有见解。大家太把自己的意愿强加于他的影评身上。</span>
          <a href="javascript:;" class="toggle_reply">...</a>
          <span class="pubdate"><a href="https://www.douban.com/people/179853490/">段润</a></span>
        </div>


      <p class="comment-text">其实我觉得，就算出现差评，就算歪楼，也不一定是坏事，总比几年前，提起一部国产纪录片，大家都一脸茫然的问“啥”要好得多。有人关注了，有人喜欢了，有人不喜欢了，总好过燕过无痕</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u84184278 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9803893" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9803921" data-cid="9803921" data-user_name="段润" data-user_url="https://www.douban.com/people/179853490/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9803893">
    <div class="avatar left">
        <a href="https://www.douban.com/people/179853490/"><img width="48" height="48" src="https://img1.doubanio.com/icon/user_normal.jpg" alt="段润"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/179853490/">段润</a>
        <span>2018-08-16 12:29:27</span>
      </div>



        <div class="reply-quote">
          <span class="short">其实我觉得，就算出现差评，就算歪楼，也不一定是坏事，总比几年前，提起一部国产纪录片，大...</span>
          <span class="all">其实我觉得，就算出现差评，就算歪楼，也不一定是坏事，总比几年前，提起一部国产纪录片，大家都一脸茫然的问“啥”要好得多。有人关注了，有人喜欢了，有人不喜欢了，总好过燕过无痕</span>
          <a href="javascript:;" class="toggle_reply">...</a>
          <span class="pubdate"><a href="https://www.douban.com/people/84184278/">木家卫</a></span>
        </div>


      <p class="comment-text">对，这是难得的，整体氛围，整体市场就是这样去提升，成长的，也需要有更多不同的声音，去推动</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u179853490 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9803921" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9803927" data-cid="9803927" data-user_name="Lanuber" data-user_url="https://www.douban.com/people/156945917/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/156945917/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u156945917-2.jpg" alt="Lanuber"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/156945917/">Lanuber</a>
        <span>2018-08-16 12:31:15</span>
      </div>



      <p class="comment-text">这种评价，恶意差评直接举报有用么</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u156945917 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9803927" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9803942" data-cid="9803942" data-user_name="弹指间" data-user_url="https://www.douban.com/people/134231759/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9759423">
    <div class="avatar left">
        <a href="https://www.douban.com/people/134231759/"><img width="48" height="48" src="https://img1.doubanio.com/icon/user_normal.jpg" alt="弹指间"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/134231759/">弹指间</a>
        <span>2018-08-16 12:37:21</span>
      </div>



        <div class="reply-quote">
          <span class="short">你说的脏话就是“放屁”？我在模仿你罢了。压根就不想和你讨论。我表达我的观点罢了。</span>
          <span class="all">你说的脏话就是“放屁”？我在模仿你罢了。压根就不想和你讨论。我表达我的观点罢了。</span>
          <span class="pubdate"><a href="https://www.douban.com/people/148323786/">Acid</a></span>
        </div>


      <p class="comment-text">就是想问楼主一声，你是不是屁闻多了？傻逼还在这聒噪</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u134231759 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9803942" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9804168" data-cid="9804168" data-user_name="笑傲人生" data-user_url="https://www.douban.com/people/a_xuan/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/a_xuan/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u40465591-33.jpg" alt="笑傲人生"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/a_xuan/">笑傲人生</a>  (2013你好 2012 你妹 爱与梦想)
        <span>2018-08-16 13:24:21</span>
      </div>



      <p class="comment-text">我去你妈了个逼啊，你看了吗？就在这里哔哔，草泥马的，你能先看看那6集，再评论电影版的好不？</p>

      <div class="op-lnks">









      </div>

      <div class="group_banned">
        <span class="gact hidden p_u40465591 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9804168" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9804254" data-cid="9804254" data-user_name="变成猫的狐狸" data-user_url="https://www.douban.com/people/60389905/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/60389905/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u60389905-4.jpg" alt="变成猫的狐狸"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/60389905/">变成猫的狐狸</a>
        <span>2018-08-16 13:45:27</span>
      </div>



      <p class="comment-text">楼主走了，走得很痛苦，火化的时候还诈了尸，一直喊着没有死，最后用铁链绑着烧完的。火很旺，烧得嘎吱嘎吱响，烧了三天三夜。追悼会播放着《今天是个好日子》，家属很坚强，一个哭的都没有，还有一个忍不住笑出了声，那天风很大，运骨灰的路上还翻了车，把骨灰盒摔碎了，刚要捧点儿骨灰，来了一辆洒水车，后来坟头堆起来三米多高，被村支书看见了铲去两米五，撒上生石灰，至今也没长草，好不容易立个碑，结果大冬天的打雷，碑都劈碎了。。。村里的人看不下去了，就把楼主挖了出来，谁也没想到他居然变成了厉鬼。说要到这里来复仇，没办法村民就找来了林正英。林正英用一把桃木剑，插进了楼主心脏，然后祭出九昧真火，准备将他火化，火化的时候眼睛掉出来了，人们说是死不瞑目。火很旺，烧的嗷嗷一直叫，烧了九九八十一天，村民还一起唱《圣诞夜》，村民狠高兴，一个哭的也没有，还有一个忍不住照了张相，林正英想让他入土为安，就给他建了大理石墓。好不容易立了个不锈钢碑。没想到国家试射东风-21导弹偏离弹道，碑都炸碎了，零碎的碑块被踩石场的工人，运去碾成了粉末，粉末糊在修的茅厕墙上，撒尿的人全部把尿射在墙上，不久就会一点一点腐蚀，全部冲进厕所和屎尿一起，一天一头种猪掉进厕所被屎尿给熏死了，楼主的灵魂进入这头猪的身体，一头新生命诞生</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u60389905 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9804254" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9804306" data-cid="9804306" data-user_name="P" data-user_url="https://www.douban.com/people/50617544/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/50617544/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u50617544-2.jpg" alt="P"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/50617544/">P</a>  (讨厌自以为是的家伙)
        <span>2018-08-16 13:58:00</span>
      </div>



      <p class="comment-text">跟你说个锤子，哈麻批</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u50617544 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9804306" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9805191" data-cid="9805191" data-user_name="扁老罗" data-user_url="https://www.douban.com/people/174983178/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/174983178/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u174983178-1.jpg" alt="扁老罗"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/174983178/">扁老罗</a>
        <span>2018-08-16 17:48:11</span>
      </div>



      <p class="comment-text">没看过剧集，就瞎评论什么玩意儿？</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u174983178 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9805191" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9806053" data-cid="9806053" data-user_name="Homo Sapiens" data-user_url="https://www.douban.com/people/181890102/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/181890102/"><img width="48" height="48" src="https://img1.doubanio.com/icon/u181890102-9.jpg" alt="Homo Sapiens"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/181890102/">Homo Sapiens</a>
        <span>2018-08-16 21:37:07</span>
      </div>



      <p class="comment-text">楼主挺住</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u181890102 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9806053" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9806063" data-cid="9806063" data-user_name="湖水中豆" data-user_url="https://www.douban.com/people/179336236/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/179336236/"><img width="48" height="48" src="https://img1.doubanio.com/icon/user_normal.jpg" alt="湖水中豆"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/179336236/">湖水中豆</a>
        <span>2018-08-16 21:40:54</span>
      </div>



      <p class="comment-text">你都说了你不了解导演，也不了解之前的剧集版，报的期待是不是显得有点搞笑呢？在你看来，这部电影是烂片，以你的上帝视角来看当然是啊。几个月前导演来过我们学校，给我们放映了这部电影，也给我们讲述了其中的很多故事。有幸和他有过一个问题的交流：你拍这部戏给他们带来了什么，给你带来了什么。何苦导演说，给他们并没有带来物质上的直接利益，更谈不上艺术上的收获，对于他们而言只不过是生活上的一小段插曲而已。而对于自己，只是带来心理上的慰藉和收获。诚然，你所看来它里面存在演绎的画面，而且何苦导演在和我们交流时也提到了一些画面的拍摄过程，难道这就是虚伪的表现嘛？一千个人心中有一千个哈姆雷特，何必要把你的想法放大，来影响他人的思考呢？这种电影不比爆米花电影，看了它之后往往会有很多感触，人的思想不一样，自然说出来的话也不一样。并没有向你挑衅或者怒骂的意味，只是认为你的言辞并不恰当。电影这种艺术性的东西，不是一朝一夕就能评论完全的，时间会给出证明!</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u179336236 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9806063" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9806081" data-cid="9806081" data-user_name="Acid" data-user_url="https://www.douban.com/people/148323786/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9806063">
    <div class="avatar left">
        <a href="https://www.douban.com/people/148323786/"><img width="48" height="48" src="https://img1.doubanio.com/icon/u148323786-8.jpg" alt="Acid"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/148323786/">Acid</a>
        <span>2018-08-16 21:46:36</span>
      </div>



        <div class="reply-quote">
          <span class="short">你都说了你不了解导演，也不了解之前的剧集版，报的期待是不是显得有点搞笑呢？在你看来，这...</span>
          <span class="all">你都说了你不了解导演，也不了解之前的剧集版，报的期待是不是显得有点搞笑呢？在你看来，这部电影是烂片，以你的上帝视角来看当然是啊。几个月前导演来过我们学校，给我们放映了这部电影，也给我们讲述了其中的很多故事。有幸和他有过一个问题的交流：你拍这部戏给他们带来了什么，给你带来了什么。何苦导演说，给他们并没有带来物质上的直接利益，更谈不上艺术上的收获，对于他们而言只不过是生活上的一小段插曲而已。而对于自己，只是带来心理上的慰藉和收获。诚然，你所看来它里面存在演绎的画面，而且何苦导演在和我们交流时也提到了一些画面的拍摄过程，难道这就是虚伪的表现嘛？一千个人心中有一千个哈姆雷特，何必要把你的想法放大，来影响他人的思考呢？这种电影不比爆米花电影，看了它之后往往会有很多感触，人的思想不一样，自然说出来的话也不一样。并没有向你挑衅或者怒骂的意味，只是认为你的言辞并不恰当。电影这种艺术性的东西，不是一朝一夕就能评论完全的，时间会给出证明!</span>
          <a href="javascript:;" class="toggle_reply">...</a>
          <span class="pubdate"><a href="https://www.douban.com/people/179336236/">湖水中豆</a></span>
        </div>


      <p class="comment-text">嗯</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u148323786 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9806081" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9806085" data-cid="9806085" data-user_name="Acid" data-user_url="https://www.douban.com/people/148323786/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9803927">
    <div class="avatar left">
        <a href="https://www.douban.com/people/148323786/"><img width="48" height="48" src="https://img1.doubanio.com/icon/u148323786-8.jpg" alt="Acid"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/148323786/">Acid</a>
        <span>2018-08-16 21:47:39</span>
      </div>



        <div class="reply-quote">
          <span class="short">这种评价，恶意差评直接举报有用么</span>
          <span class="all">这种评价，恶意差评直接举报有用么</span>
          <span class="pubdate"><a href="https://www.douban.com/people/156945917/">Lanuber</a></span>
        </div>


      <p class="comment-text">试试呗</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u148323786 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9806085" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9806106" data-cid="9806106" data-user_name="Acid" data-user_url="https://www.douban.com/people/148323786/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9803271">
    <div class="avatar left">
        <a href="https://www.douban.com/people/148323786/"><img width="48" height="48" src="https://img1.doubanio.com/icon/u148323786-8.jpg" alt="Acid"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/148323786/">Acid</a>
        <span>2018-08-16 21:52:00</span>
      </div>



        <div class="reply-quote">
          <span class="short">楼主所理解的纪录片概念太狭隘了，从梅里爱排演的新闻片，到弗拉哈迪的《北方的纳努克》，摆...</span>
          <span class="all">楼主所理解的纪录片概念太狭隘了，从梅里爱排演的新闻片，到弗拉哈迪的《北方的纳努克》，摆拍还原是纪录片的一部分。其他的内容还没看过电影，不敢评价，就这一部分而言，几乎没有纪录片是完全的事实记载，哪怕新闻片，编导的主观因素也会影响剪辑，毕竟电影是人的艺术，要体现人的思想</span>
          <a href="javascript:;" class="toggle_reply">...</a>
          <span class="pubdate"><a href="https://www.douban.com/people/84184278/">木家卫</a></span>
        </div>


      <p class="comment-text">主观因素当然是应该有的，也是无法避免的。我在看完这部片子以后跟老师谈过真实性的问题。她说你有没有想过，你看到的一切都是导演的主观蒙太奇。我觉得很有道理。但是过度煽情和明显的引导，还有情节上的断裂等等问题，我觉得都是无法忍受的，也是不应该有的。现在看我当时的想法确实是狭隘偏激了点。但是多数观点现在我还是坚守的。可能以后我拍了片子会有不一样的看法吧。到时候我可能会回来改。我也不是很清楚了。</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u148323786 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9806106" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9806110" data-cid="9806110" data-user_name="Acid" data-user_url="https://www.douban.com/people/148323786/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9801607">
    <div class="avatar left">
        <a href="https://www.douban.com/people/148323786/"><img width="48" height="48" src="https://img1.doubanio.com/icon/u148323786-8.jpg" alt="Acid"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/148323786/">Acid</a>
        <span>2018-08-16 21:52:52</span>
      </div>



        <div class="reply-quote">
          <span class="short">是不是重庆人？看过山城棒棒军吗？</span>
          <span class="all">是不是重庆人？看过山城棒棒军吗？</span>
          <span class="pubdate"><a href="https://www.douban.com/people/163250141/">滑之多恶好</a></span>
        </div>


      <p class="comment-text">不是，最近听说了这部片子准备看。</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u148323786 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9806110" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9806112" data-cid="9806112" data-user_name="Acid" data-user_url="https://www.douban.com/people/148323786/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9803184">
    <div class="avatar left">
        <a href="https://www.douban.com/people/148323786/"><img width="48" height="48" src="https://img1.doubanio.com/icon/u148323786-8.jpg" alt="Acid"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/148323786/">Acid</a>
        <span>2018-08-16 21:53:20</span>
      </div>



        <div class="reply-quote">
          <span class="short">你有个屁的艺术鉴赏能力，垃圾</span>
          <span class="all">你有个屁的艺术鉴赏能力，垃圾</span>
          <span class="pubdate"><a href="https://www.douban.com/people/144238862/">斑马</a></span>
        </div>


      <p class="comment-text">见笑了，我没有鉴赏能力，放屁的权利还是有的。</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u148323786 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9806112" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9806124" data-cid="9806124" data-user_name="Acid" data-user_url="https://www.douban.com/people/148323786/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9801450">
    <div class="avatar left">
        <a href="https://www.douban.com/people/148323786/"><img width="48" height="48" src="https://img1.doubanio.com/icon/u148323786-8.jpg" alt="Acid"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/148323786/">Acid</a>
        <span>2018-08-16 21:55:40</span>
      </div>



        <div class="reply-quote">
          <span class="short">我觉得楼主和我想的差不多，就是言辞比较严重，作品结尾和植入确实是败笔，但还不至于一星哈</span>
          <span class="all">我觉得楼主和我想的差不多，就是言辞比较严重，作品结尾和植入确实是败笔，但还不至于一星哈</span>
          <span class="pubdate"><a href="https://www.douban.com/people/103390292/">辉__</a></span>
        </div>


      <p class="comment-text">偏激了，有点情绪在里面。 很多人都是我这个看法，我就想发个长评说说。</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u148323786 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9806124" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9806125" data-cid="9806125" data-user_name="Acid" data-user_url="https://www.douban.com/people/148323786/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9800703">
    <div class="avatar left">
        <a href="https://www.douban.com/people/148323786/"><img width="48" height="48" src="https://img1.doubanio.com/icon/u148323786-8.jpg" alt="Acid"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/148323786/">Acid</a>
        <span>2018-08-16 21:55:57</span>
      </div>



        <div class="reply-quote">
          <span class="short">不想回复你！不值得！</span>
          <span class="all">不想回复你！不值得！</span>
          <span class="pubdate"><a href="https://www.douban.com/people/94177249/">青春待出售</a></span>
        </div>


      <p class="comment-text">没求你啊？</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u148323786 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9806125" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9806126" data-cid="9806126" data-user_name="Acid" data-user_url="https://www.douban.com/people/148323786/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9799486">
    <div class="avatar left">
        <a href="https://www.douban.com/people/148323786/"><img width="48" height="48" src="https://img1.doubanio.com/icon/u148323786-8.jpg" alt="Acid"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/148323786/">Acid</a>
        <span>2018-08-16 21:56:07</span>
      </div>



        <div class="reply-quote">
          <span class="short">建议楼主去看下原版纪录片</span>
          <span class="all">建议楼主去看下原版纪录片</span>
          <span class="pubdate"><a href="https://www.douban.com/people/61041468/">乌拉拉</a></span>
        </div>


      <p class="comment-text">嗯，一定会看。</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u148323786 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9806126" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9806131" data-cid="9806131" data-user_name="Acid" data-user_url="https://www.douban.com/people/148323786/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9798017">
    <div class="avatar left">
        <a href="https://www.douban.com/people/148323786/"><img width="48" height="48" src="https://img1.doubanio.com/icon/u148323786-8.jpg" alt="Acid"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/148323786/">Acid</a>
        <span>2018-08-16 21:58:05</span>
      </div>



        <div class="reply-quote">
          <span class="short">你不喜欢电影版  但是你也得一尊重  你只是在刻意发泄你的不喜欢而已 搞的自己很牛逼一样，就...</span>
          <span class="all">你不喜欢电影版  但是你也得一尊重  你只是在刻意发泄你的不喜欢而已 搞的自己很牛逼一样，就你一个人会影评吗？ 什么样的是烂片？  在你眼中就是你不喜欢的就是烂片  什么可以摆拍  故意煽情？ 还好意思说宁可花八小时去看一部不带任何色彩的作品，也不愿意看故意煽情的片子 你是在搞笑吗？</span>
          <a href="javascript:;" class="toggle_reply">...</a>
          <span class="pubdate"><a href="https://www.douban.com/people/131784501/">谁的爱温暖了我</a></span>
        </div>


      <p class="comment-text">我就是这个看法，我宁可看八个小时乏味没有什么艺术价值的片子也不看它。我就是装逼，行了？</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u148323786 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9806131" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9806141" data-cid="9806141" data-user_name="Acid" data-user_url="https://www.douban.com/people/148323786/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9794191">
    <div class="avatar left">
        <a href="https://www.douban.com/people/148323786/"><img width="48" height="48" src="https://img1.doubanio.com/icon/u148323786-8.jpg" alt="Acid"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/148323786/">Acid</a>
        <span>2018-08-16 22:00:40</span>
      </div>



        <div class="reply-quote">
          <span class="short">说纪录片必须克制的，怕是没听说过《意志的胜利》，煽动性很强，却是影史经典</span>
          <span class="all">说纪录片必须克制的，怕是没听说过《意志的胜利》，煽动性很强，却是影史经典</span>
          <span class="pubdate"><a href="https://www.douban.com/people/65569388/">大海里的针</a></span>
        </div>


      <p class="comment-text">我回去看一下然后再和你讨论</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u148323786 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9806141" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9806147" data-cid="9806147" data-user_name="Acid" data-user_url="https://www.douban.com/people/148323786/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9794191">
    <div class="avatar left">
        <a href="https://www.douban.com/people/148323786/"><img width="48" height="48" src="https://img1.doubanio.com/icon/u148323786-8.jpg" alt="Acid"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/148323786/">Acid</a>
        <span>2018-08-16 22:01:46</span>
      </div>



        <div class="reply-quote">
          <span class="short">说纪录片必须克制的，怕是没听说过《意志的胜利》，煽动性很强，却是影史经典</span>
          <span class="all">说纪录片必须克制的，怕是没听说过《意志的胜利》，煽动性很强，却是影史经典</span>
          <span class="pubdate"><a href="https://www.douban.com/people/65569388/">大海里的针</a></span>
        </div>


      <p class="comment-text">到没说必须克制，只是我欣赏克制。主要是这个片子的煽情是一种很低级的煽情。断裂式的。甚至会影响节奏。</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u148323786 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9806147" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9806339" data-cid="9806339" data-user_name="寻觅" data-user_url="https://www.douban.com/people/132150518/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/132150518/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u132150518-1.jpg" alt="寻觅"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/132150518/">寻觅</a>
        <span>2018-08-16 23:06:46</span>
      </div>



      <p class="comment-text">客观点说，楼主的确应该去看一下全版的纪录片，你会有不同的认识的。但是另一方面看电影的时候，我也在思考，对于一个没有看过全版纪录片的观众，只看电影又会有怎么样的认识。楼主的观点，估计就可以代表这绝大部分观众吧，只不过楼主说得刻薄了一些。其实我们这些老观众都明白，何苦导演并不是专业的，所以很多技法上面的确很平淡，我可以容忍与包容。而作为电影，刻意的煽情、闪回、特写，这就让没看过的观众莫名其妙了，我们不能强行要求这部分观众也去接受。我愿意为何苦的刻苦与牺牲买单，所以专门买票去电影院支持了导演。但是空荡荡的影院也让我更加清楚，点映几天了，但是却还没有形成口碑效应，大概率又要票房扑街了，这个就真和导演的才华有关了。</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u132150518 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9806339" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9806365" data-cid="9806365" data-user_name="滑之多恶好" data-user_url="https://www.douban.com/people/163250141/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9806110">
    <div class="avatar left">
        <a href="https://www.douban.com/people/163250141/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u163250141-6.jpg" alt="滑之多恶好"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/163250141/">滑之多恶好</a>
        <span>2018-08-16 23:15:02</span>
      </div>



        <div class="reply-quote">
          <span class="short">不是，最近听说了这部片子准备看。</span>
          <span class="all">不是，最近听说了这部片子准备看。</span>
          <span class="pubdate"><a href="https://www.douban.com/people/148323786/">Acid</a></span>
        </div>


      <p class="comment-text">可能重庆人看了感触比较深吧，也不能怪楼主。我自己也看了你文中提到的几部纪录片，不同类型的都有看，个人认为这部纪录片视角虽然主观，但是陈述的都非常纪实，每个人物都是有血有肉的，比你文中提到的某几部可能更贴近现实，虽然我们体会不到别人的人生和生活环境，但是至少我们能真切的看到。每个人看问题的视角和考虑问题的因素及方向都不同，但不妨碍我们主观或是客观的评价，没其他意思。</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u163250141 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9806365" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9806400" data-cid="9806400" data-user_name="慢先森" data-user_url="https://www.douban.com/people/mr.slow/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="0">
    <div class="avatar left">
        <a href="https://www.douban.com/people/mr.slow/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u1079160-93.jpg" alt="慢先森"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/mr.slow/">慢先森</a>
        <span>2018-08-16 23:24:15</span>
      </div>



      <p class="comment-text">有朋友说这是部纪实电影，不是纪录片。我觉得这个定位比较准。这是部有温度的电影，不是冷冰冰的纪录片。不必用学院派的眼光来看，太严厉苛刻。导演介入人物生活并且改变了人物命运有什么不好？难道只有一味反映他们有多苦被抛弃来黑ZF来叫好吗？最后部分只是反应他们现在的真实状况。为啥就不能接受呢？为啥就一定要那么阴暗呢？</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u1079160 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9806400" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9807266" data-cid="9807266" data-user_name="程寒城" data-user_url="https://www.douban.com/people/142835614/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9757339">
    <div class="avatar left">
        <a href="https://www.douban.com/people/142835614/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u142835614-3.jpg" alt="程寒城"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/142835614/">程寒城</a>
        <span>2018-08-17 07:08:35</span>
      </div>



        <div class="reply-quote">
          <span class="short">谢谢你的回复，暴露了你的粗鲁！一个张口就说脏话的人，连我说什么都看不懂的人，嗯，我现在...</span>
          <span class="all">谢谢你的回复，暴露了你的粗鲁！一个张口就说脏话的人，连我说什么都看不懂的人，嗯，我现在不奇怪为什么一部大家都说好的电影你却评价如此之低了，猫眼里打四分那个人应该也是你吧～你的言行暴露了你的修养素质品味，以后我不会再与你对话～最后表达一个观点，我不管它是纪录片还是爱情片还是商业片还是………………只要好看，只要能让我有思考，能打动我，我就喜欢～我接受一切新的创意和手法！我相信大家也会一样，你不接受没关系，别看就好了，谢谢！</span>
          <a href="javascript:;" class="toggle_reply">...</a>
          <span class="pubdate"><a href="https://www.douban.com/people/175009559/">立春</a></span>
        </div>


      <p class="comment-text">你是导演本人吧！</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u142835614 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9807266" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>



  <div class="comment-item" id="9807315" data-cid="9807315" data-user_name="立春" data-user_url="https://www.douban.com/people/175009559/" data-target_id="9574214" data-target_kind="1012" data-ref_cid="9807266">
    <div class="avatar left">
        <a href="https://www.douban.com/people/175009559/"><img width="48" height="48" src="https://img1.doubanio.com/icon/user_normal.jpg" alt="立春"></a>
    </div>
    <div class="content report-comment">
      <div class="header">
        <a href="https://www.douban.com/people/175009559/">立春</a>
        <span>2018-08-17 07:39:59</span>
      </div>



        <div class="reply-quote">
          <span class="short">你是导演本人吧！</span>
          <span class="all">你是导演本人吧！</span>
          <span class="pubdate"><a href="https://www.douban.com/people/142835614/">程寒城</a></span>
        </div>


      <p class="comment-text">头号铁杆粉丝无疑了</p>

      <div class="op-lnks">

        <a href="https://www.douban.com/doubanapp/" class="comment-source" target="_blank">          来自豆瓣App        </a>








      </div>

      <div class="group_banned">
        <span class="gact hidden p_u175009559 p_admin p_intern fright">&gt;
        <a href="javascript:;" data-cid="9807315" class="remove_comment">删除</a>
        </span>
      </div>
    </div>
  </div>
</body>
</html>'''
soup = BeautifulSoup(html, 'html.parser')

filename = '我为什么厌恶电影版《最后的棒棒》.txt'
for comment in soup.find_all('p'):
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(comment.contents[0] + '\n')
f = open(filename, encoding='utf-8')
data = pd.read_csv(f, encoding='utf-8')

comment = jieba.cut(str(data), cut_all=False)
wl_space_split = " ".join(comment)

background_Image = plt.imread('lan.jpg')
stopwords = STOPWORDS.copy()

wc = WordCloud(width=1024, height=768, background_color='white',
               mask=background_Image, font_path="C:\Windows\Fonts\simfang.ttf",
               stopwords=stopwords, max_font_size=400,
               random_state=50)
wc.generate_from_text(wl_space_split)
plt.imshow(wc)
plt.axis('off')
plt.show()
wc.to_file(r'world_cloud.jpg')


def all_list(arr):
    result = {}
    for i in arr:
        if i in result.keys():
            result[i] = result[i] + 1
        else:
            result[i] = 1
    return result


comment_file = '评论席.txt'
for auth_div in soup.find_all(name='div', attrs={"class": "header"}):
    with open(comment_file, 'a', encoding='utf-8') as f:
        f.write(auth_div.a.contents[0] + '\n')

f = open(comment_file, encoding='utf-8')
auth_old_data = []
for line in f:
    auth_old_data.append(line.strip('\n'))
auth_rate = all_list(auth_old_data)

attr = list(auth_rate.keys())
v2 = list(auth_rate.values())

bar = Bar("发布评论")
bar.add("作者" + str(len(v2)), attr, v2, is_stack=True, xaxis_rotate=1, yaxix_min=1.2,
        xaxis_interval=0, is_splitline_show=False)
bar.render("发布评论.html")

pie = Pie("发布评论分布情况", title_pos='left', width=1000, title_text_size=40)
pie.add("发布评论分布情况", attr, v2, center=[50, 50], is_random=False, radius=[20, 50], rosetype='area',
        is_legend_show=False, is_label_show=True, label_text_size=12)
pie.render('发布评论分布情况.html')

acid_comment = ''
for auth_div in soup.find_all(name='div', attrs={"class": "header"}):
    if auth_div.a.contents[0] == 'Acid':
        acid_comment += auth_div.parent.p.contents[0]

comment = jieba.cut(acid_comment, cut_all=False)
wl_space_split = " ".join(comment)

background_Image = plt.imread('dog.jpg')
stopwords = STOPWORDS.copy()

wc = WordCloud(width=1024, height=768, background_color='white',
               mask=background_Image, font_path="C:\Windows\Fonts\simfang.ttf",
               stopwords=stopwords, max_font_size=400,
               random_state=50)
wc.generate_from_text(wl_space_split)
plt.imshow(wc)
plt.axis('off')
plt.show()
wc.to_file(r'acid.jpg')
