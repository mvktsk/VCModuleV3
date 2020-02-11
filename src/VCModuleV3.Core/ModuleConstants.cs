using System.Collections.Generic;
using VirtoCommerce.Platform.Core.Settings;

namespace VCModuleV3.Core
{
    public class ModuleConstants
    {
        public static class Security
        {
            public static class Permissions
            {
                public const string Read = "VCModuleV3:read";
                public const string Create = "VCModuleV3:create";
                public const string Access = "VCModuleV3:access";
                public const string Update = "VCModuleV3:update";
                public const string Delete = "VCModuleV3:delete";

                public static string[] AllPermissions = { Read, Create, Access, Update, Delete };
            }
        }

        public static class Settings
        {
            public static class General
            {
                public static SettingDescriptor CustomerReviewsEnabled = new SettingDescriptor
                {
                    Name = "VCModuleV3.VCModuleV3Enabled",
                    GroupName = "Store|General",
                    ValueType = SettingValueType.Boolean,
                    DefaultValue = false
                };

                public static SettingDescriptor CustomerReviewsPassword = new SettingDescriptor
                {
                    Name = "VCModuleV3.VCModuleV3Password",
                    GroupName = "Store|Advanced",
                    ValueType = SettingValueType.SecureString,
                    DefaultValue = "qwerty"
                };

                public static IEnumerable<SettingDescriptor> AllSettings
                {
                    get
                    {
                        yield return CustomerReviewsEnabled;
                        yield return CustomerReviewsPassword;
                    }
                }
            }

            public static IEnumerable<SettingDescriptor> AllSettings
            {
                get
                {
                    return General.AllSettings;
                }
            }
        }

    }
}
