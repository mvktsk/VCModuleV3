using VCModuleV3.Core;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;

namespace VCModuleV3.Web.Controllers.Api
{
    [Route("api/VCModuleV3")]
    public class VCModuleV3Controller : Controller
    {
        // GET: api/VC2module
        [HttpGet]
        [Route("")]
        [Authorize(ModuleConstants.Security.Permissions.Read)]
        public ActionResult<string> Get()
        {
            return Ok(new { result = "Hello world!" });
        }
    }
}
