$("a.row-toggler").click(function () {
    $(this).closest("tr").next("tr.content-row").toggle();
});