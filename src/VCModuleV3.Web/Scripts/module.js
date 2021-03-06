//Call this to register our module to main application
var moduleTemplateName = "VCModuleV3";

if (AppDependencies !== undefined) {
    AppDependencies.push(moduleTemplateName);
}

angular.module(moduleTemplateName, [])
.config(['$stateProvider', 
    function ($stateProvider) {
        $stateProvider
            .state('workspace.vcModuleV3', {
                url: '/vCModuleV3',
                templateUrl: '$(Platform)/Scripts/common/templates/home.tpl.html',
                controller: [
                    'platformWebApp.bladeNavigationService', function (bladeNavigationService) {
                        var newBlade = {
                            id: 'reviewsList',
                            controller: 'vCModuleV3.helloWorldController',
                            template: 'Modules/$(VCModuleV3)/Scripts/blades/hello-world.tpl.html',
                            isClosingDisabled: true
                        };
                        bladeNavigationService.showBlade(newBlade);
                    }
                ]
            });
    }
])
.run(['platformWebApp.mainMenuService', '$state',
    function (mainMenuService, $state) {
        //Register module in main menu
        var menuItem = {
            path: 'browse/vCModuleV3',
            icon: 'fa fa-comments',
            title: 'VCModuleV3 module',
            priority: 100,
            action: function () { $state.go('workspace.vCModuleV3') },
            permission: 'VCModuleV3:read'
        };
        mainMenuService.addMenuItem(menuItem);
    }
]);
