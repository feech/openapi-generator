// <auto-generated>
/*
 * OpenAPI Petstore
 *
 * This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\
 *
 * The version of the OpenAPI document: 1.0.0
 * Generated by: https://github.com/openapitools/openapi-generator.git
 */

using System;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.IO;
using System.Runtime.Serialization;
using System.Text;
using System.Text.RegularExpressions;
using System.Text.Json;
using System.Text.Json.Serialization;
using System.ComponentModel.DataAnnotations;
using OpenAPIClientUtils = Org.OpenAPITools.Client.ClientUtils;

namespace Org.OpenAPITools.Model
{
    /// <summary>
    /// OuterComposite
    /// </summary>
    public partial class OuterComposite : IEquatable<OuterComposite>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="OuterComposite" /> class.
        /// </summary>
        /// <param name="myNumber">myNumber</param>
        /// <param name="myString">myString</param>
        /// <param name="myBoolean">myBoolean</param>
        public OuterComposite(decimal myNumber = default, string myString = default, bool myBoolean = default)
        {
            MyNumber = myNumber;
            MyString = myString;
            MyBoolean = myBoolean;
        }

        /// <summary>
        /// Gets or Sets MyNumber
        /// </summary>
        [JsonPropertyName("my_number")]
        public decimal MyNumber { get; set; }

        /// <summary>
        /// Gets or Sets MyString
        /// </summary>
        [JsonPropertyName("my_string")]
        public string MyString { get; set; }

        /// <summary>
        /// Gets or Sets MyBoolean
        /// </summary>
        [JsonPropertyName("my_boolean")]
        public bool MyBoolean { get; set; }

        /// <summary>
        /// Gets or Sets additional properties
        /// </summary>
        [JsonExtensionData]
        public Dictionary<string, JsonElement> AdditionalProperties { get; set; } = new Dictionary<string, JsonElement>();

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            sb.Append("class OuterComposite {\n");
            sb.Append("  MyNumber: ").Append(MyNumber).Append("\n");
            sb.Append("  MyString: ").Append(MyString).Append("\n");
            sb.Append("  MyBoolean: ").Append(MyBoolean).Append("\n");
            sb.Append("  AdditionalProperties: ").Append(AdditionalProperties).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="input">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object input)
        {
            return OpenAPIClientUtils.compareLogic.Compare(this, input as OuterComposite).AreEqual;
        }

        /// <summary>
        /// Returns true if OuterComposite instances are equal
        /// </summary>
        /// <param name="input">Instance of OuterComposite to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(OuterComposite input)
        {
            return OpenAPIClientUtils.compareLogic.Compare(this, input).AreEqual;
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                int hashCode = 41;
                hashCode = (hashCode * 59) + this.MyNumber.GetHashCode();
                if (this.MyString != null)
                {
                    hashCode = (hashCode * 59) + this.MyString.GetHashCode();
                }
                hashCode = (hashCode * 59) + this.MyBoolean.GetHashCode();
                if (this.AdditionalProperties != null)
                {
                    hashCode = (hashCode * 59) + this.AdditionalProperties.GetHashCode();
                }
                return hashCode;
            }
        }

        /// <summary>
        /// To validate all properties of the instance
        /// </summary>
        /// <param name="validationContext">Validation context</param>
        /// <returns>Validation Result</returns>
        public IEnumerable<System.ComponentModel.DataAnnotations.ValidationResult> Validate(ValidationContext validationContext)
        {
            yield break;
        }
    }

}
