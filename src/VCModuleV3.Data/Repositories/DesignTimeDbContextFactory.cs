using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Design;

namespace VCModuleV3.Data.Repositories
{
    public class DesignTimeDbContextFactory : IDesignTimeDbContextFactory<VCModuleV3DbContext>
    {
        public VCModuleV3DbContext CreateDbContext(string[] args)
        {
            var builder = new DbContextOptionsBuilder<VCModuleV3DbContext>();

            builder.UseSqlServer("Data Source=(local);Initial Catalog=VirtoCommerce3;Persist Security Info=True;User ID=virto;Password=virto;MultipleActiveResultSets=True;Connect Timeout=30");

            return new VCModuleV3DbContext(builder.Options);
        }
    }
}
