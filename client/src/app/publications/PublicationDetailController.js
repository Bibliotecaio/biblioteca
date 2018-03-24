angular.module('PublicationDetailController', [
  'ui.router'
])

.controller('PublicationDetailController',
  function PublicationDetailController($state, $stateParams, dataService, pageTitleService) {
    let vm = this;
    
    let documentId = parseInt($stateParams.id, 10);
    
    let getDocument = function (id) {
      dataService.publications.get({'id': id})
        .$promise.then(function(response) {
        // success
        vm.publication = response;
        pageTitleService.publish(response.headline);
        
      }, function(errResponse) {});
    };
    
    // Initial title TODO: Improve this hack
    pageTitleService.publish('Публикации');
    
    // Display data from server
    getDocument(documentId);
});
