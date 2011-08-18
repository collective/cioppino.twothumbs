jQuery(function(jq){

    jq('#content').delegate(".thumb-rating form input", "click", (function(event){
        event.preventDefault();
        var me = jq(this);
        var form = me.closest('form');
        if(form.hasClass('disabled')) {
                // Can't rate, show info box
                var container = form.closest('.thumb-rating');
                var login = container.find('.login-to-rate');
                if(login.length===0) {
                    container.append('<div>').children().last().hide().addClass('login-to-rate').load('./login-to-rate dl', function() {
			    var me = $(this);
                            me.slideDown().find('.close-link').click(function(event) {
                                event.preventDefault(); 
				$(this).closest('.login-to-rate').slideUp(function() {$(this).remove();});
			    });
 
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
