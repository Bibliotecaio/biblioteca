angular.module('documentViewerDirective', [
	'pageTitleService',
	'storageLinkFilter',
	'ui.router'
])
	
  
.directive('documentViewerDirective',
  function documentViewerDirective($timeout, $location, $state, $stateParams, localStorageService, dataService, pageTitleService) {
    return {
      restrict: 'E',
      replace: true,
      scope: false,
      transclude: false,
      template: '<div id="document-viewer"></div>',
      link: function (scope, elem, attrs) {
       
      	let document_id = parseInt($stateParams.id, 10);
      	
        let constructBook = function (data) {
          scope.currentDocument = DV.load(
            data,
            {
              container: '#document-viewer',
              sidebar: true,
              text: false,
              responsive: true,
              responsiveOffset: 0
            }
          );

        };
        
				let getDocument = function (id) {
      		dataService.documentViewer.get({'id': id})
						.$promise.then(function(response) {
        		// success
        		pageTitleService.publish(response.title);
        		constructBook(response);
      		}, function(errResponse) {});
    		};
      
				getDocument(document_id);
        
        //$timeout(function(){
        //  constructBook();
        //}, 2000);
      }
    };
});
