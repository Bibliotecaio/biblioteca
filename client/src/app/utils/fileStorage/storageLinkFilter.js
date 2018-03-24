angular.module('storageLinkFilter', [
])


.filter('storageLink', function storageLinkFilter(ENV) {

  function storageLink(fileId) {
    return `${ ENV.fileStorageEndpoint }/${ fileId }`;
  }
  return function(fileId){
    return storageLink(fileId);
  };
});
