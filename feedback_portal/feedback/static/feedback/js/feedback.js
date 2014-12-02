$(document).ready(function(){
//  Check Radio-box
    $("input:radio").attr("checked", false);
    $('input').click(function () {
        $("span").removeClass('checked');
        $(this).parent().addClass('checked');
    });

    $('input:radio').change(
    function(){
        var userRating = this.value;
        //alert(userRating);

        // send this userRating variable to calculate the rating of the prof
    });
});