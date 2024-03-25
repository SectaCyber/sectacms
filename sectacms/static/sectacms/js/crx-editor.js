/*
Wagtail Secta (https://www.Secta.dev/cms/)
Copyright 2018-2023 secta LLC
License: https://github.com/SectaCyber/sectacms/blob/main/LICENSE
@license magnet:?xt=urn:btih:c80d50af7d3db9be66a4d0a86db0286e4fd33292&dn=bsd-3-clause.txt BSD-3-Clause
*/

$(document).ready(function(){
    $(document).on('click', '.Secta-collapsible button', function(){
        var $target = $(this).parent().find('.Secta-collapsible-target');

        if (!$(this).parent().hasClass('collapsed')) {
            $(this).parent().addClass('collapsed');
            $target.hide('fast');
        } else {
            $(this).parent().removeClass('collapsed');
            $target.show('fast');
        }
    });
});

/* @license-end */
