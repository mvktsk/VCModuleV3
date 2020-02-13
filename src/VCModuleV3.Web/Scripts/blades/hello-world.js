angular.module('VCModuleV3')
    .controller('VCModuleV3.helloWorldController', ['$scope', 'VCModuleV3.api', function ($scope, api) {

            var blade = $scope.blade;
            blade.title = 'VCModuleV3.blades.hello-world.title';
            blade.headIcon = 'fa-comments';

            blade.refresh = function () {
                api.get(function (data) {
                    blade.data = data.result;
                    blade.isLoading = false;
                });
            };

            blade.refresh();
    }]);
