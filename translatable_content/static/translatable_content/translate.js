// $.ajax({
//    type: "POST",
//    url: "/translation/",
//    data: jsonData,
////    contentType: "application/json; charset=utf-8",
////    dataType: "json",
//    success: function(data) {
//		var win = window.open();
//    	win.document.write(data);
//    },
//    error: function(msg) {
//        //alert(error);
//    }
//});

jQuery(document).ready(function () {
    $('a.transstr').on('click', function (e) {
       
       url1 = document.URL.split('/');
       var id = url1[url1.length-2];
       var model = url1[url1.length-3];
       var app = url1[url1.length-4];
       var field = this.id 
       //alert(this.id);
       //var ind = this.id.indexOf("_set-");
       var ind = this.id.split("-");
       if (ind.length == 3)
       {
       		
			var model = ind[0].split("_")[0];
			var field = ind[2];
			var the_id = ind[0]+ '-' +ind [1] + '-id';
			id = $('#id_'+the_id).val() ;
       }
      
       direct_to ='/translatable_content/str/'+ app + '/' + model+ '/' + id+ '/' +field +'/';
       e.preventDefault();
        /* We pre-open the popup in the submit, since it was generated from a "click" event, so no popup block happens */
        authWindow = window.open('about:blank', '', 'left=20,top=20,width=1000,height=500,toolbar=0,resizable=1');
        m_url = direct_to,
        $.ajax({
            url: m_url,
            //type: "POST",
            //data: {"json": JSON.stringify({"url": 'http://' + e.target.value + '.com'})}
//            success: function (url) {
//                //window.close();
//                success = true
//            },
//            error: function () {#newinlineimage_set-0-id
//                e.preventDefault();
//            }
			
        }).done(function (url) {
            /* This is where the magic happens, we simply redirec the popup to the new authorize URL that we received from the server */
            authWindow.location.replace(m_url);
        })
        .always(function () {
            /* You can poll if the window got closed here, and so a refresh on the main page, or another AJAX call for example */
        });
    })


	 $('a.transtext').on('click', function (e) {
       
       url1 = document.URL.split('/');
       var id = url1[url1.length-2];
       var model = url1[url1.length-3];
       var app = url1[url1.length-4];
       var field = this.id 
       //alert(this.id);
       //var ind = this.id.indexOf("_set-");
       var ind = this.id.split("-");
       if (ind.length == 3)
       {
       		
			var model = ind[0].split("_")[0];
			var field = ind[2];
			var the_id = ind[0]+ '-' +ind [1] + '-id';
			id = $('#id_'+the_id).val() ;
       }
      
       direct_to ='/translatable_content/text/'+ app + '/' + model+ '/' + id+ '/' +field +'/';
       e.preventDefault();
        /* We pre-open the popup in the submit, since it was generated from a "click" event, so no popup block happens */
        authWindow = window.open('about:blank', '', 'left=20,top=20,width=1024,height=1000,toolbar=0,resizable=1');
        m_url = direct_to,
        $.ajax({
            url: m_url,
            //type: "POST",
            //data: {"json": JSON.stringify({"url": 'http://' + e.target.value + '.com'})}
//            success: function (url) {
//                //window.close();
//                success = true
//            },
//            error: function () {#newinlineimage_set-0-id
//                e.preventDefault();
//            }
			
        }).done(function (url) {
            /* This is where the magic happens, we simply redirec the popup to the new authorize URL that we received from the server */
            authWindow.location.replace(m_url);
        })
        .always(function () {
            /* You can poll if the window got closed here, and so a refresh on the main page, or another AJAX call for example */
        });
    })




})
