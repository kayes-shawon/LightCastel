
// GoTo
$('a[data-toggle="GoTo"]').click(function(event){
    var path = window.location.pathname + window.location.hash;
    console.log(path)

    if (path.indexOf('in-the-media') === -1 && path.indexOf('/about') === -1) {
        event.preventDefault();
        var willGo = $(this).attr('href');
        var targetOffset = $('a[href*="' + willGo + '"]').offset().top - 150;
        $('html, body').animate({scrollTop: targetOffset}, 1000);
    }

});





// Member Talked
$('.member_talked').click(function(event) {
    event.preventDefault();

    const $this = $(this);
    const MemberTalked = $this.data('member_talked');
    var message = $this.data('message');
    const Member = jQuery.parseJSON(JSON.stringify(MemberTalked));
    const ModalMember = $('#modal-member');
    
    const tamplate = `<div class="member clearfix">
                    <a class="pull-left member-img" href="#">
                        <img class="media-object" src="`+ Member.img +`" alt="Image">
                    </a>
                    
                    <h4 class="margin-top-0">`+ Member.full_name +`</h4>
                    <h6>`+ Member.designation +`</h5>

                    <p class="member-talked">`+ message +`</p>
                </div>`;

    ModalMember.find('.modal-body').html(tamplate);
    ModalMember.modal('show');
});

// News Letter
$('#FormNewsletter').formValidation({
    framework: 'bootstrap',
    icon: { valid: 'glyphicon glyphicon-ok', invalid: 'glyphicon glyphicon-remove', validating: 'glyphicon glyphicon-refresh' },
    fields: {
        email: {
            validators: {
                notEmpty: { message: 'The email address is required' },
                emailAddress: { message: 'The input is not a valid email address' }
            }
        }
    }
})
.on('success.form.fv', function(e) {
    e.preventDefault();
    var $form = $(e.target);

    $.ajax({
        url: $form.attr('action'),
        type: $form.attr('method'),
        data: $form.serialize(),
        dataType: 'json',
        success: function(response) {
            if(response.message == "subscribed successfully"){
                var modalSuccessText = '<h3 class="text-center">Thanks for subscription</h3>';
                $('#modal-auto').find('.modal-body').html(modalSuccessText);
                $('#modal-auto').modal('show');    
            }else{
                alert("Whoops something went wrong. Please try again.");
            }
        }
    });

});

// Contact Form
$('#ContactForm').formValidation({
    framework: 'bootstrap',
    icon: { valid: 'glyphicon glyphicon-ok', invalid: 'glyphicon glyphicon-remove', validating: 'glyphicon glyphicon-refresh' },
    fields: {
        name: { validators: { notEmpty: { message: 'Please write your full name' } } },
        email: {
            validators: {
                notEmpty: { message: 'The email address is required' },
                emailAddress: { message: 'Sorry this email is not a valid email format.' }
            }
        },
        phone: { validators: { notEmpty: { message: 'The phone number is required' } } },
        message: { validators: { notEmpty: { message: 'The message is required' } } }
    }
})
.on('success.form.fv', function(e) {
    e.preventDefault();
    var $form = $(e.target);

    $.ajax({
        url: $form.attr('action'),
        type: $form.attr('method'),
        data: $form.serialize(),
        dataType: 'json',
        success: function(response) {
            if(response.message == "success"){
                var modalSuccessText = '<h3 class="text-center">Thank you for your message! We hope to get back to you in 2 business days.</h3>';
                $('#modal-auto').find('.modal-body').html(modalSuccessText);
                $('#modal-auto').modal('show');
            }else{
                alert("Whoops something went wrong. Please try again.");
            }
        }
    });

});