$("li.nav-item a").on("click", function () {
    $(this).parent().addClass("active");
    $(this).parent().closest("active").removeClass("active");
});