using EntityFrameworkCore.Triggers;
using Microsoft.EntityFrameworkCore;

namespace VCModuleV3.Data.Repositories
{
    public class VCModuleV3DbContext : DbContextWithTriggers
    {
        public VCModuleV3DbContext(DbContextOptions<VCModuleV3DbContext> options)
          : base(options)
        {
        }

        protected VCModuleV3DbContext(DbContextOptions options)
            : base(options)
        {
        }
        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            //        modelBuilder.Entity<MyModuleEntity>().ToTable("MyModule").HasKey(x => x.Id);
            //        modelBuilder.Entity<MyModuleEntity>().Property(x => x.Id).HasMaxLength(128);
            //        base.OnModelCreating(modelBuilder);
        }
    }
}
