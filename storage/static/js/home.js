$(".clipboard_copy").on("click", function() {
    copy_clipboard($("#contract_address").get());
});

function copy_clipboard(element) {
    console.log("here");
    var $temp = $("<input>");
    $("body").append($temp);
    $temp.val($(element).text()).select();
    document.execCommand("copy");
    $(".copied_message").css({"display": "flex"});
    $(".copied_message").delay(2000).fadeOut();
    $temp.remove();
}
