package org.openapitools

import org.springframework.context.annotation.Bean
import org.springframework.stereotype.Controller
import org.springframework.web.bind.annotation.RequestMapping
import org.springframework.web.bind.annotation.ResponseBody
import org.springframework.web.bind.annotation.GetMapping

/**
 * Home redirection to OpenAPI api documentation
 */
@Controller
class HomeController {
    private val apiDocsPath = "/v2/api-docs"

    @GetMapping(value = ["/swagger-config.yaml"], produces = ["text/plain"])
    @ResponseBody
    fun swaggerConfig(): String = "url: $apiDocsPath\n"

    @RequestMapping("/")
    fun index(): String = "redirect:swagger-ui.html"
}
