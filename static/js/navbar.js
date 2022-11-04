// $(".nav-item").on("click", (e) => {
//     console.log(`${this.className} click`)
//     $(this).closest(".active").removeClass("active");
//     $(this).addClass("active");
//     e.preventDefault();
// });
$("li.nav-item a").on("click", function () {
    $(this).parent().addClass("active");
    $(this).parent().closest("active").removeClass("active");
});
