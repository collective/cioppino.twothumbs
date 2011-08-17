jQuery(function(jq){

    jq('#content').delegate(".thumb-rating form input", "click", (function(event){
        event.preventDefault();
        var me = jq(this);
        var form = me.closest('form');
        if(form.hasClass('disabled')) {
                var container = form.closest('.thumb-rating');
                var login = container.find('.login-to-rate');
                if(login.length>0) {
                    login.stop().hide().slideDown();
                } else {
                    container.append('<div>').children().last().hide().load('./login-to-rate div', function() {
                            $(this).slideDown();
                    });
                }
                return;
        }
        me.blur();
        var action = me.attr('name');
        var summary = form.siblings('.like-summary');
        var upResults = summary.find('.total-thumbs-up .tally-total');
        var downResults = summary.find('.total-thumbs-down .tally-total');
        if (form){
            jq.post(form.attr("action"),action+'=FOOBAR&ajax=1', 
                function(data) {
                    /* update the text */
                    upResults.text(data.ups);
                    downResults.text(data.downs);
                    
                    /* update the class */
                    form.find('.thumbs-down').removeClass('selected');
                    form.find('.thumbs-up').removeClass('selected');
                    if (action == 'form.lovinit' && data.mine==1) {
                        form.find('.thumbs-up').addClass('selected');
                    } else if (action == 'form.hatedit' && data.mine==-1) {
                        form.find('.thumbs-down').addClass('selected');
                    }
                }, 'json');

        }
    }));
});
