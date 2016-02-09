jQuery(function(jq){

	jq('body').delegate('.thumb-rating form input', 'click', function(event) {
		event.preventDefault();
		var me = jq(this);
		var form = me.closest('form');
		if(form.hasClass('disabled')) {
			// Can't rate, show info box
			var container = form.closest('.thumb-rating');
			var login = container.find('.twothumbs-feedback');
			if(login.length===0) {
				jq('<div>').addClass('twothumbs-feedback').hide().load('./login-to-rate', function() {
					var me = jq(this);
					me.slideDown().find('.close-link').click(function(event) {
						event.preventDefault();
						jq(this).closest('.twothumbs-feedback').slideUp();
					});

				}).appendTo(container);
			} else {
				login.slideDown();
			}
			return;
		} else {
			// Can rate, go ahead!
			me.blur();
			var action = me.attr('name');
			var upResults = form.find('.total-thumbs-up .tally-total');
			var downResults = form.find('.total-thumbs-down .tally-total');
			var auth_key = form.find('input[name="_authenticator"]').val();
			if (form){
				jq.post(form.attr("action"),action+'=FOOBAR&ajax=1&_authenticator='+auth_key, function(data) {
					/* update the text */
					upResults.text(data.ups);
					downResults.text(data.downs);

					/* update the class */
					form.find('.thumbs-down').removeClass('selected');
					form.find('.thumbs-up').removeClass('selected');
					if (data.action=='like') {
						form.find('.thumbs-up').addClass('selected');
					} else if (data.action=='dislike') {
						form.find('.thumbs-down').addClass('selected');
					}

					/* extra feedback */
					var feedback = form.find('.twothumbs-feedback');
					if(feedback.length) {
						feedback.remove();
					}
					var id = 'ttf-' + (new Date()).getTime();
					jq('<div>').attr('id', id).addClass('twothumbs-feedback').html(data.msg).
					prepend('<a class="close-link" title="' + data.close + '" href="#">&nbsp;</a>').
					appendTo(form).hide().slideDown().find('.close-link').click(function(event) {
						event.preventDefault();
						jq(this).closest('.twothumbs-feedback').slideUp();
					});
					setTimeout((function() {
						jq('#' + id).slideUp();
					}), 2000);
				}, 'json');
			}
		}
	});

});
