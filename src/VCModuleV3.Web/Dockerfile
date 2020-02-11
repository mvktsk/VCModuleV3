#See https://aka.ms/containerfastmode to understand how Visual Studio uses this Dockerfile to build your images for faster debugging.

FROM mcr.microsoft.com/dotnet/core/aspnet:3.1-buster-slim AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/core/sdk:3.1-buster AS build
WORKDIR /src
COPY ["src/VCModuleV3.Web/VCModuleV3.Web.csproj", "src/VCModuleV3.Web/"]
RUN dotnet restore "src/VCModuleV3.Web/VCModuleV3.Web.csproj"
COPY . .
WORKDIR "/src/VCModuleV3.Web"
RUN dotnet build "VCModuleV3.Web.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "VCModuleV3.Web.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "WebApplication2.dll"]