

$(document).ready(function(){

	//reveal side menu
	var siteWrapperWidth = $('.site-wrapper').outerWidth();

	$('.site-wrapper').css({ width: siteWrapperWidth, right: '0' })


	$('#menuBar').click(function() {
	 		$('.site-wrapper').toggleClass('show-menu')
	})

	$('.list-group-item').click(function () {
			$('.site-wrapper').removeClass('show-menu')
	})


	//Dropdown sign in/sign up forms
	// $('#signUpContainer, #signInContainer').hide()

	$('#signUpButton').click(function() {
		$('#signUpContainer').animate({height: 'toggle'})

		if( $('#signInContainer').is(':visible') ) {
	 		 $('#signInContainer').hide()
	  }
	})

	$('#signInButton').click(function() {
		$('#signInContainer').animate({height: 'toggle'})

		if( $('#signUpContainer').is(':visible') ) {
	 		 $('#signUpContainer').hide()
	  }
	})


	//Floating labels effect 
	$('.form-control').focus(function() {
			$('label').animate({
				position: 'absolute',
				top: '0px',
				color: '#01579B',
				paddingLeft: '0px'
			})

		
	})

	$('input').blur(function() {
		if($('input').val().length > 0) {
				$('label').animate({
					position: 'absolute',
					top: '0px',
					color: '#01579B',
					paddingLeft: '0px'
				})
		} else {
			$('label').animate({
				position: 'relative',
				top: '42px',
				color: '#B0BEC5',
				paddingLeft: '16px'
			})
		}
	})


});
