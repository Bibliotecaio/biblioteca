angular.module('dataService', [
  'ngResource'
])
  
.factory('dataService',
  function dataService($resource, ENV) {
    return {
      login: $resource(
        `${ ENV.apiEndpoint }/api/login/`),
      logout: $resource(
        `${ ENV.apiEndpoint }/api/logout/`),
      documents: $resource(
        `${ ENV.apiEndpoint }/api/documents/:id/`),
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
