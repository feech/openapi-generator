/*
 * OpenAPI Petstore
 * This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\
 *
 * OpenAPI spec version: 1.0.0
 *
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

package org.openapitools.client.api;


import java.util.Map;
import org.junit.Ignore;
import org.junit.Test;
import org.openapitools.client.ApiException;
import org.openapitools.client.model.Order;

/** API tests for StoreApi */
@Ignore
public class StoreApiTest {

    private final StoreApi api = new StoreApi();

    /**
     * Delete purchase order by ID
     *
     * <p>For valid response try integer IDs with value &lt; 1000. Anything above 1000 or
     * nonintegers will generate API errors
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteOrderTest() throws ApiException {
        String orderId = null;
        api.deleteOrder(orderId);

        // TODO: test validations
    }

    /**
     * Returns pet inventories by status
     *
     * <p>Returns a map of status codes to quantities
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getInventoryTest() throws ApiException {
        Map<String, Integer> response = api.getInventory();

        // TODO: test validations
    }

    /**
     * Find purchase order by ID
     *
     * <p>For valid response try integer IDs with value &lt;&#x3D; 5 or &gt; 10. Other values will
     * generated exceptions
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getOrderByIdTest() throws ApiException {
        Long orderId = null;
        Order response = api.getOrderById(orderId);

        // TODO: test validations
    }

    /**
     * Place an order for a pet
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void placeOrderTest() throws ApiException {
        Order body = null;
        Order response = api.placeOrder(body);

        // TODO: test validations
    }
}
