angular.module('VCModuleV3')
    .controller('VCModuleV3.helloWorldController', ['$scope', 'VCModuleV3.api', function ($scope, reviewsApi) {
            $scope.uiGridConstants = uiGridConstants;

            var blade = $scope.blade;
            blade.title = 'VCModuleV3.blades.hello-world.title';
            blade.headIcon = 'fa-comments';

            blade.refresh = function () {
                blade.isLoading = true;
                reviewsApi.search(blade.getSearchCriteria(), function (data) {
                    blade.isLoading = false;
                    blade.data = data.result;
                });
            };

            blade.refresh();

    }]);
