#See https://aka.ms/containerfastmode to understand how Visual Studio uses this Dockerfile to build your images for faster debugging.

FROM mcr.microsoft.com/dotnet/core/aspnet:3.1-buster-slim AS base
RUN apt-get update
RUN apt-get -yq install wget \
    && apt-get -yq install unzip
RUN wget -q "https://github.com/VirtoCommerce/vc-platform/releases/download/3.0.0-rc.3/VirtoCommerce.Platform.3.0.0-rc.3.1.zip" \
    && unzip -q VirtoCommerce.Platform.3.0.0-rc.3.1.zip -d vc-platform-3 \
    && rm VirtoCommerce.Platform.3.0.0-rc.3.1.zip
RUN mkdir /vc-platform-3/Modules
RUN ln -s /app /vc-platform-3/Modules/VCModuleV3
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
