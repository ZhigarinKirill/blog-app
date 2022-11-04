$("a.row-toggler").on("click", function () {
    $(this).closest("tr").next("tr.content-row").toggle();
});
