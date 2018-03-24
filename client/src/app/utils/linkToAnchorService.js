angular.module('linkToAnchorService', [
])

.service('linkToAnchorService',
    function linkToAnhcorService($location, $anchorScroll) {
      this.toLink = function(id) {
        $anchorScroll();
      };
    });
