var s = 0;
var activityIds = [];

var i = activityIds.length;
var k = 0;
//添加一个节点用于打开子页面
$('body').prepend('<iframe src="" width="900px" height="610px" style="border: 0px;" id="listReload" name="listReload"></iframe>');
var first = true;
var second = false;
var doLoad = false;
var firstDo = true;
//过滤参数
var filterKeyList = [
    '男用', '女用', '杜蕾斯', '课程', '避孕套', '安全套',
    '白酒', '二锅头', '中国电信', '中国联通', '中国移动',
    '流量卡', '上网卡', '万门大学', '零基础', '检测', '盐',
    '情趣', '吃鸡', '假睫毛', '和田玉', '紧致', '缩阴',
    '考卷', '黑头', '病毒', '水杨酸', '痘痘', '霉菌',
    '痘印', '洗面奶', '古龙', '鸡眼', '保健品', '青春痘', '数据线',
    '过滤网', '眼药水', '止痒', '湿疹', '祛痘', '电子烟', '精油',
    '卫裤', '脓肿', '膏药', '性功能', '狐臭'
];
//过滤提供份数
var filterNumber = 10;
//过滤价格
var filterPrice = 15;
//定义加载函数
$("iframe").load(function() {
    if (firstDo) return;
    doLoad = true;
    second = true;
    sendActition();
});
setInterval(function() {
    if (k < i) {
        firstDo = false;
        console.log('处理第' + (k + 1) + '个');
        s = activityIds[k];
        if (first == second && doLoad) {
            sendActition();
        }
        $('iframe').attr('src', 'https://try.jd.com/' + s + '.html#this');
    } else {
        console.log('完成');
    }
}, 5600);

var sendActition = function() {
    //Google浏览器获取门店id
    // var shopId = window.frames["listReload"].document.getElementById("_shopId").value;
    //EDEGE浏览器获取门店id
    var shopId = document.getElementById('listReload').contentWindow.document.getElementById('_shopId').value;
    console.log('关注店铺Id:' + shopId);
    //提供份数
    var offerCount = document.getElementById('listReload').contentWindow.document.getElementsByClassName('try-info')[0].getElementsByTagName('b')[0].innerText;
    //价格
    var cost = document.getElementById('listReload').contentWindow.document.getElementsByClassName('price')[0].getElementsByTagName('b')[0] ? document.getElementById('listReload').contentWindow.document.getElementsByClassName('price')[0].getElementsByTagName('b')[0].innerText : 0;
    //标题
    var productName = document.getElementById('listReload').contentWindow.document.getElementsByClassName('name')[0].getElementsByTagName('span')[0].innerText;

    if (offerCount > filterNumber || cost < filterPrice) {
        k++;
        second = false;
        doLoad = false;
        console.log('产品被过滤。价格：' + cost + ' ,提供数量：' + offerCount);
        return;
    }
    for (let filter_index = 0; filter_index < filterKeyList.length; filter_index++) {
        const element = filterKeyList[filter_index];
        if (productName.indexOf(element) > -1) {
            k++;
            second = false;
            doLoad = false;
            console.log('产品低级，被过滤。产品名称：' + productName + ' ,过滤条件：' + element);
            return;
        }
    }
    $.ajax({
        type: "GET",
        dataType: "JSON",
        async: false,
        url: 'https://try.jd.com/migrate/follow?_s=pc&venderId=' + shopId,
        complete: function() {
            console.log('申请试用:' + s);
            $.ajax({
                type: "GET",
                dataType: "JSON",
                async: false,
                url: 'https://try.jd.com/migrate/apply?activityId=' + s + '&source=0',
                success: function(data) {
                    if (!data || !data.success) {
                        if (!data.message || data.message == '您的申请已成功提交，请勿重复申请…' || data.message == '当前活动为测试活动，不能申请！' || data.message == '还没到申请时间！' || data.message == '当前活动不能申请！' || data == '{"bottom":null}') {
                            k++;
                            second = false;
                            doLoad = false;
                        }
                        console.log(s + data.message);
                        return;
                    }
                    if (data && data.success) {
                        k++;
                        second = false;
                        doLoad = false;
                        console.log(s + data.message);
                    }
                }
            });
        }
    });
};