$(document).ready(function () {
    $("#ajax-text-me").click(function() {
        $.ajax({
            type: 'GET',
            async: true,
            url: '/get_movie_ajax/',
            // data: $('#search').serialize(),
            success: function(data) {
                var doc = $.parseHTML(data.html);
                $('#main').html(doc);
            },
            dataType: 'json',
        });
    });
});
