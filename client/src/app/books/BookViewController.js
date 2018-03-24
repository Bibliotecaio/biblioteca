angular.module('BookViewController', [
  'sticky',
  'ngTextTruncate',
  'ui.select',
  'ui.router'
])

.controller('BookViewController',
  function BookViewController($stateParams, dataService, localStorageService, pageTitleService) {
    let vm = this;
    
    let document_id = parseInt($stateParams.id, 10);
    
    let getDocument = function (id) {
      dataService.documents.get({'id': id})
        .$promise.then(function(response) {
        // success
        vm.doc = response;
        pageTitleService.publish(response.title);
        localStorageService.remove('doc');
        localStorageService.set('doc', response);
      }, function(errResponse) {});
    };
    
    getDocument(document_id);
    
    
});
