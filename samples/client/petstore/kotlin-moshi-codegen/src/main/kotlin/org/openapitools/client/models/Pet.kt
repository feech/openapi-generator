/**
 *
 * Please note:
 * This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * Do not edit this file manually.
 *
 */

@file:Suppress(
    "ArrayInDataClass",
    "EnumEntryName",
    "RemoveRedundantQualifierName",
    "UnusedImport"
)

package org.openapitools.client.models

import org.openapitools.client.models.Category
import org.openapitools.client.models.Tag

import com.squareup.moshi.Json
import com.squareup.moshi.JsonClass

/**
 * A pet for sale in the pet store
 *
 * @param name 
 * @param photoUrls 
 * @param id 
 * @param category 
 * @param tags 
 * @param status pet status in the store
 */
@JsonClass(generateAdapter = true)
data class Pet (

    @Json(name = "name")
    val name: kotlin.String,

    @Json(name = "photoUrls")
    val photoUrls: kotlin.collections.List<kotlin.String>,

    @Json(name = "id")
    val id: kotlin.Long? = null,

    @Json(name = "category")
    val category: Category? = null,

    @Json(name = "tags")
    val tags: kotlin.collections.List<Tag>? = null,

    /* pet status in the store */
    @Json(name = "status")
    val status: Pet.Status? = null

) {

    /**
     * pet status in the store
     *
     * Values: available,pending,sold
     */
    enum class Status(val value: kotlin.String) {
        @Json(name = "available") available("available"),
        @Json(name = "pending") pending("pending"),
        @Json(name = "sold") sold("sold");
    }
}

