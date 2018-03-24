angular.module('documentViewerDirective', [
	'pageTitleService',
	'storageLinkFilter',
	'ui.router'
])
	
  
.directive('documentViewerDirective',
  function documentViewerDirective($timeout, $location, $state, $stateParams, localStorageService, pageTitleService, ENV) {
    return {
      restrict: 'E',
      replace: true,
      scope: false,
      transclude: false,
      template: '<div id="document-viewer"></div>',
      link: function ($scope, elem, attrs) {
      
      let d = {
	"id": "82753-lefler-thesis",
	"title": "Приходской листок",
	"pages": 129,
	"description": "A Master's Thesis on the phenomenon of \"LOLSPEAK\" and its origin in image macros.",
	"source": null,
	"created_at": "Tue, 10 Jan 2012 20:20:36 +0000",
	"updated_at": "Fri, 09 Feb 2018 16:40:27 +0000",
	"canonical_url": "https://www.documentcloud.org/documents/282753-lefler-thesis.html",
	"language": "ru",
	"file_hash": null,
	"contributor": "Ted Han",
	"contributor_slug": "2258-ted-han",
	"contributor_documents_url": "https://www.documentcloud.org/public/search/Account:2258-ted-han",
	"contributor_organization": "Foo",
	"contributor_organization_slug": "dcloud",
	"contributor_organization_documents_url": "https://www.documentcloud.org/public/search/Group:dcloud",
	"display_language": "ru",
	"resources": {
		"pdf": "https://assets.documentcloud.org/documents/282753/lefler-thesis.pdf",
		"text": "https://assets.documentcloud.org/documents/282753/lefler-thesis.txt",
		"thumbnail": "https://assets.documentcloud.org/documents/282753/pages/lefler-thesis-p1-thumbnail.gif",
		"search": "https://www.documentcloud.org/documents/282753/search.json?q={query}",
		"print_annotations": "https://www.documentcloud.org/notes/print?docs[]=282753",
		"translations_url": "https://www.documentcloud.org/translations/{realm}/{language}",
		"page": {
			"image": "https://assets.documentcloud.org/documents/282753/pages/lefler-thesis-p{page}-{size}.gif",
			"text": "https://www.documentcloud.org/documents/282753/pages/lefler-thesis-p{page}.txt"
		},
		"published_url": "https://www.documentcloud.org/documents/282753-lefler-thesis.html"
	},
	"sections": [],
	"data": {},
	"annotations": []
};
        
        let constructBook = function () {
          $scope.currentDocument = DV.load(
            d,
            {
              container: '#document-viewer',
              sidebar: true
            }
          );

        };
        constructBook();
        //$timeout(function(){
        //  constructBook();
        //}, 2000);
      }
    };
});
