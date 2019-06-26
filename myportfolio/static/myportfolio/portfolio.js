$(function(){

    // モーダルウィンドウが開くときの処理    
    $(".modalOpen").click(function(){
        var href = $(this).attr("href");
                
        $(href).addClass("is-active");
        return false;
    });
     
    // モーダルウィンドウが閉じるときの処理    
    $(".delete").click(function(){
        $(this).parents(".modal").removeClass("is-active");
        return false;
    });  
        
});