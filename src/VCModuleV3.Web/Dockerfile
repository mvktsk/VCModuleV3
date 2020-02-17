#See https://aka.ms/containerfastmode to understand how Visual Studio uses this Dockerfile to build your images for faster debugging.

FROM mcr.microsoft.com/dotnet/core/aspnet:3.1-buster-slim AS base
RUN apt-get update
RUN apt-get -yq install wget \
    && apt-get -yq install unzip\
    && apt-get -yq install python3
RUN wget -q "https://github.com/VirtoCommerce/vc-platform/releases/download/3.0.0-rc.3/VirtoCommerce.Platform.3.0.0-rc.3.1.zip" \
    && unzip -q VirtoCommerce.Platform.3.0.0-rc.3.1.zip -d vc-platform-3 \
    && rm VirtoCommerce.Platform.3.0.0-rc.3.1.zip
RUN mkdir /vc-platform-3/Modules
#RUN mkdir /py
RUN ln -s /app /vc-platform-3/Modules/VCModuleV3
#COPY InstallLatestModules.py /py
WORKDIR /vc-platform-3/Modules
#RUN python3 /py/InstallLatestModules.py

RUN wget -q "https://github.com/VirtoCommerce/vc-module-tax/releases/download/3.0.0-rc.3/VirtoCommerce.Tax_3.0.0-rc.3.zip" && unzip -q VirtoCommerce.Tax_3.0.0-rc.3.zip -d /vc-platform-3/Modules/VirtoCommerce.Tax && rm VirtoCommerce.Tax_3.0.0-rc.3.zip
RUN wget -q "https://github.com/VirtoCommerce/vc-module-subscription/releases/download/3.0.0-rc.3/VirtoCommerce.Subscription_3.0.0-rc.3.zip" && unzip -q VirtoCommerce.Subscription_3.0.0-rc.3.zip -d /vc-platform-3/Modules/VirtoCommerce.Subscription && rm VirtoCommerce.Subscription_3.0.0-rc.3.zip
RUN wget -q "https://github.com/VirtoCommerce/vc-module-sitemaps/releases/download/3.0.0-rc.3/VirtoCommerce.Sitemaps_3.0.0-rc.3.zip" && unzip -q VirtoCommerce.Sitemaps_3.0.0-rc.3.zip -d /vc-platform-3/Modules/VirtoCommerce.Sitemaps && rm VirtoCommerce.Sitemaps_3.0.0-rc.3.zip
RUN wget -q "https://github.com/VirtoCommerce/vc-module-notification/releases/download/3.0.0-rc.3/VirtoCommerce.Notifications_3.0.0-rc.3.zip" && unzip -q VirtoCommerce.Notifications_3.0.0-rc.3.zip -d /vc-platform-3/Modules/VirtoCommerce.Notifications && rm VirtoCommerce.Notifications_3.0.0-rc.3.zip
RUN wget -q "https://github.com/VirtoCommerce/vc-module-marketing/releases/download/3.0.0-rc.3/VirtoCommerce.Marketing_3.0.0-rc.3.zip" && unzip -q VirtoCommerce.Marketing_3.0.0-rc.3.zip -d /vc-platform-3/Modules/VirtoCommerce.Marketing && rm VirtoCommerce.Marketing_3.0.0-rc.3.zip
RUN wget -q "https://github.com/VirtoCommerce/vc-module-lucene-search/releases/download/3.0.0-rc.3/VirtoCommerce.LuceneSearch_3.0.0-rc.3.zip" && unzip -q VirtoCommerce.LuceneSearch_3.0.0-rc.3.zip -d /vc-platform-3/Modules/VirtoCommerce.LuceneSearch && rm VirtoCommerce.LuceneSearch_3.0.0-rc.3.zip
RUN wget -q "https://github.com/VirtoCommerce/vc-module-inventory/releases/download/3.0.0-rc.3/VirtoCommerce.Inventory_3.0.0-rc.3.zip" && unzip -q VirtoCommerce.Inventory_3.0.0-rc.3.zip -d /vc-platform-3/Modules/VirtoCommerce.Inventory && rm VirtoCommerce.Inventory_3.0.0-rc.3.zip
RUN wget -q "https://github.com/VirtoCommerce/vc-module-image-tools/releases/download/3.0.0-rc.3/VirtoCommerce.ImageTools_3.0.0-rc.3.zip" && unzip -q VirtoCommerce.ImageTools_3.0.0-rc.3.zip -d /vc-platform-3/Modules/VirtoCommerce.ImageTools && rm VirtoCommerce.ImageTools_3.0.0-rc.3.zip
RUN wget -q "https://github.com/VirtoCommerce/vc-module-elastic-search/releases/download/3.0.0-rc.3/VirtoCommerce.ElasticSearch_3.0.0-rc.3.zip" && unzip -q VirtoCommerce.ElasticSearch_3.0.0-rc.3.zip -d /vc-platform-3/Modules/VirtoCommerce.ElasticSearch && rm VirtoCommerce.ElasticSearch_3.0.0-rc.3.zip
RUN wget -q "https://github.com/VirtoCommerce/vc-module-content/releases/download/3.0.0-rc.3/VirtoCommerce.Content_3.0.0-rc.3.zip" && unzip -q VirtoCommerce.Content_3.0.0-rc.3.zip -d /vc-platform-3/Modules/VirtoCommerce.Content && rm VirtoCommerce.Content_3.0.0-rc.3.zip
RUN wget -q "https://github.com/VirtoCommerce/vc-module-catalog/releases/download/3.0.0-rc.3/VirtoCommerce.Catalog_3.0.0-rc.3.zip" && unzip -q VirtoCommerce.Catalog_3.0.0-rc.3.zip -d /vc-platform-3/Modules/VirtoCommerce.Catalog && rm VirtoCommerce.Catalog_3.0.0-rc.3.zip
RUN wget -q "https://github.com/VirtoCommerce/vc-module-export/releases/download/3.0.0-rc.3/VirtoCommerce.Export_3.0.0-rc.3.zip" && unzip -q VirtoCommerce.Export_3.0.0-rc.3.zip -d /vc-platform-3/Modules/VirtoCommerce.Export && rm VirtoCommerce.Export_3.0.0-rc.3.zip
RUN wget -q "https://github.com/VirtoCommerce/vc-module-search/releases/download/3.0.0-rc.3/VirtoCommerce.Search_3.0.0-rc.3.zip" && unzip -q VirtoCommerce.Search_3.0.0-rc.3.zip -d /vc-platform-3/Modules/VirtoCommerce.Search && rm VirtoCommerce.Search_3.0.0-rc.3.zip
RUN wget -q "https://github.com/VirtoCommerce/vc-module-azure-search/releases/download/3.0.0-rc.3/VirtoCommerce.AzureSearch_3.0.0-rc.3.zip" && unzip -q VirtoCommerce.AzureSearch_3.0.0-rc.3.zip -d /vc-platform-3/Modules/VirtoCommerce.AzureSearch && rm VirtoCommerce.AzureSearch_3.0.0-rc.3.zip
RUN wget -q "https://github.com/VirtoCommerce/vc-module-core/releases/download/3.0.0-rc.3/VirtoCommerce.Core_3.0.0-rc.3.zip" && unzip -q VirtoCommerce.Core_3.0.0-rc.3.zip -d /vc-platform-3/Modules/VirtoCommerce.Core && rm VirtoCommerce.Core_3.0.0-rc.3.zip
RUN wget -q "https://github.com/VirtoCommerce/vc-module-customer/releases/download/3.0.0-rc.3/VirtoCommerce.Customer_3.0.0-rc.3.zip" && unzip -q VirtoCommerce.Customer_3.0.0-rc.3.zip -d /vc-platform-3/Modules/VirtoCommerce.Customer && rm VirtoCommerce.Customer_3.0.0-rc.3.zip
RUN wget -q "https://github.com/VirtoCommerce/vc-module-order/releases/download/3.0.0-rc.3/VirtoCommerce.Orders_3.0.0-rc.3.zip" && unzip -q VirtoCommerce.Orders_3.0.0-rc.3.zip -d /vc-platform-3/Modules/VirtoCommerce.Orders && rm VirtoCommerce.Orders_3.0.0-rc.3.zip
RUN wget -q "https://github.com/VirtoCommerce/vc-module-cart/releases/download/3.0.0-rc.3/VirtoCommerce.Cart_3.0.0-rc.3.zip" && unzip -q VirtoCommerce.Cart_3.0.0-rc.3.zip -d /vc-platform-3/Modules/VirtoCommerce.Cart && rm VirtoCommerce.Cart_3.0.0-rc.3.zip
RUN wget -q "https://github.com/VirtoCommerce/vc-module-shipping/releases/download/3.0.0-rc.3/VirtoCommerce.Shipping_3.0.0-rc.3.zip" && unzip -q VirtoCommerce.Shipping_3.0.0-rc.3.zip -d /vc-platform-3/Modules/VirtoCommerce.Shipping && rm VirtoCommerce.Shipping_3.0.0-rc.3.zip
RUN wget -q "https://github.com/VirtoCommerce/vc-module-payment/releases/download/3.0.0-rc.3/VirtoCommerce.Payment_3.0.0-rc.3.zip" && unzip -q VirtoCommerce.Payment_3.0.0-rc.3.zip -d /vc-platform-3/Modules/VirtoCommerce.Payment  && rm VirtoCommerce.Payment_3.0.0-rc.3.zip
RUN wget -q "https://github.com/VirtoCommerce/vc-module-store/releases/download/3.0.0-rc.3/VirtoCommerce.Store_3.0.0-rc.3.zip" && unzip -q VirtoCommerce.Store_3.0.0-rc.3.zip -d /vc-platform-3/Modules/VirtoCommerce.Store && rm VirtoCommerce.Store_3.0.0-rc.3.zip
RUN wget -q "https://github.com/VirtoCommerce/vc-module-pricing/releases/download/3.0.0-rc.3/VirtoCommerce.Pricing_3.0.0-rc.3.zip" && unzip -q VirtoCommerce.Pricing_3.0.0-rc.3.zip -d /vc-platform-3/Modules/VirtoCommerce.Pricing && rm VirtoCommerce.Pricing_3.0.0-rc.3.zip
WORKDIR /vc-platform-3
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/core/sdk:3.1-buster AS build
WORKDIR /src
COPY ["src/VCModuleV3.Web/VCModuleV3.Web.csproj", "src/VCModuleV3.Web/"]
COPY ["src/VCModuleV3.Core/VCModuleV3.Core.csproj", "src/VCModuleV3.Core/"]
COPY ["src/VCModuleV3.Data/VCModuleV3.Data.csproj", "src/VCModuleV3.Data/"]
RUN dotnet restore "src/VCModuleV3.Web/VCModuleV3.Web.csproj"
COPY . .
WORKDIR "/src/src/VCModuleV3.Web"
RUN dotnet build "VCModuleV3.Web.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "VCModuleV3.Web.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "VCModuleV3.Web.dll"]
