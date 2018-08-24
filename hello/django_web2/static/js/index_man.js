

(function(){
	$(".reveal-s-h li").hover(function(){
		$(this).children(".a-img").show().end().siblings().children(".a-img").hide();
	});
})();

var fodTime = 0; //tab菜单切换参数
function tagOver(name,x,n){
 clearTimeout(fodTime);
 fodTime = setTimeout(function(){
 setTab(name,x,n)
 },100);
}
function setTab(name,x,n){
 for(i=1;i<=n;i++){
 var menu=document.getElementById(name+"_"+i);
 var con=document.getElementById("con_"+name+"_"+i);
 menu.className=i==x?"hover":"";
 con.style.display=i==x?"block":"none";
 }
}
/**
 * 鼠标滑出清除原先的滑动效果
 */
function tagOut(){
 clearTimeout(fodTime);
 fodTime=0;
}


$.fn.jdSonny=function(option,callback){
				if(typeof option=="function"){callback=option;option={};};
				var s=$.extend({current:"curr",delay:50,index:0},option||{});
				var _this=this;
				var timer=null;
				$.each(this,function(n){
					$(this).bind("mouseover",function(){
						if(timer!=null)clearTimeout(timer);
						var obj=$(this);
						timer=setTimeout(function(){
							_this.eq(s.index).removeClass(s.current);
							s.index=n;
							_this.eq(s.index).addClass(s.current);
							if (callback){callback(obj);}
						},s.delay);
					})
				})
			}

			$(".pages_w_topul").eq(0).find("li").jdSonny({current:"fore"},function(object){
				object.find("img").each(function(){
					var src2=$(this).attr("src2");
					$(this).attr("src",src2);
					$(this).removeAttr("src2");
				})
			});

			$(".pages_w_topul").eq(1).find("li").jdSonny({current:"fore"});

			$(".pages_w_topul").eq(2).find("li").jdSonny({current:"fore"});
/**
 * 鼠标滑出清除原先的滑动效果
 */
function tagOut(){
 clearTimeout(fodTime);
 fodTime=0;
}


$.fn.jdSonny=function(option,callback){
				if(typeof option=="function"){callback=option;option={};};
				var s=$.extend({current:"curr",delay:50,index:0},option||{});
				var _this=this;
				var timer=null;
				$.each(this,function(n){
					$(this).bind("mouseover",function(){
						if(timer!=null)clearTimeout(timer);
						var obj=$(this);
						timer=setTimeout(function(){
							_this.eq(s.index).removeClass(s.current);
							s.index=n;
							_this.eq(s.index).addClass(s.current);
							if (callback){callback(obj);}
						},s.delay);
					})
				})
			}

			$(".pages_w_topul2").eq(0).find("li").jdSonny({current:"fore"},function(object){
				object.find("img").each(function(){
					var src2=$(this).attr("src2");
					$(this).attr("src",src2);
					$(this).removeAttr("src2");
				})
			});

			$(".pages_w_topul2").eq(1).find("li").jdSonny({current:"fore"});

			$(".pages_w_topul2").eq(2).find("li").jdSonny({current:"fore"});
