package com.erp.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import java.util.List;
import java.util.Map;

@RestController
public class InventoryController {

    @Autowired
    private JdbcTemplate jdbcTemplate;

    /**
     * Queries 'inventory' table where quantity <= reorder_level.
     * Returns List of Maps representing JSON objects.
     */
    @GetMapping("/api/inventory/alerts")
    public List<Map<String, Object>> getAlerts() {
        String sql = "SELECT id, product_name, quantity, reorder_level FROM inventory WHERE quantity <= reorder_level";
        return jdbcTemplate.queryForList(sql);
    }
}
