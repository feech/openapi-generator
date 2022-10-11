package org.openapitools.model

import java.util.Objects
import com.fasterxml.jackson.annotation.JsonProperty
import javax.validation.constraints.DecimalMax
import javax.validation.constraints.DecimalMin
import javax.validation.constraints.Email
import javax.validation.constraints.Max
import javax.validation.constraints.Min
import javax.validation.constraints.NotNull
import javax.validation.constraints.Pattern
import javax.validation.constraints.Size
import javax.validation.Valid
import io.swagger.v3.oas.annotations.media.Schema

/**
 * Describes the result of uploading an image resource
 * @param code 
 * @param type 
 * @param message 
 */
data class ModelApiResponse(

    @Schema(example = "null", description = "")
    @field:JsonProperty("code") var code: kotlin.Int? = null,

    @Schema(example = "null", description = "")
    @field:JsonProperty("type") var type: kotlin.String? = null,

    @Schema(example = "null", description = "")
    @field:JsonProperty("message") var message: kotlin.String? = null
) {

}

