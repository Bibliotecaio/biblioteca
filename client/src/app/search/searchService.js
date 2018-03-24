angular.module('searchService', [
])

.service('searchService',
    function searchService($location, linkToAnchorService) {
      
      this.submitQueries = function (page, queries) {
          let searchObj = {page: page, q: queries};
          $location.path('/search/').search(searchObj);
          linkToAnchorService.toLink('top-search');
        };
      });
