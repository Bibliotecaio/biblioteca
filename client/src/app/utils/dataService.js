angular.module('dataService', [
  'ngResource'
])
  
.factory('dataService',
  function dataService($resource, ENV) {
    return {
      documents: $resource(
        `${ ENV.apiEndpoint }/api/documents/:id/`),
      documentViewer: $resource(
        `${ ENV.apiEndpoint }/api/document-viewer/:id/`),
      randomDocuments: $resource(
        `${ ENV.apiEndpoint }/api/documents-random/`),
      addDocument: $resource(
        `${ ENV.apiEndpoint }/api/add-document/`),
      initialFilter: $resource(
        `${ ENV.apiEndpoint }/api/initial-filters/`),
      publications: $resource(
        `${ ENV.apiEndpoint }/api/publications/:id/`),
      search: $resource(
        `${ ENV.apiEndpoint }/api/search/`),
    };
  });
