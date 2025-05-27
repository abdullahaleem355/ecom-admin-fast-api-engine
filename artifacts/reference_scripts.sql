
INSERT INTO categories (category_id, category_name, category_desc, last_updated_by, last_updated_at) VALUES
(1, 'Electronics', 'Devices and gadgets', 'admin', '2025-05-18 12:00:00'),
(2, 'Books', 'Printed and digital books', 'admin', '2025-05-18 12:00:00'),
(3, 'Clothing', 'Apparel and accessories', 'admin', '2025-05-18 12:00:00');

INSERT INTO products (product_id, product_name, product_desc, price, category_id, last_updated_by, last_updated_at) VALUES
(101, 'iPhone 14', 'Apple smartphone with A15 chip', 999.99, 1, 'admin', '2025-05-01 10:10:00'),
(102, 'Dell XPS 13', 'Compact and powerful ultrabook', 1249.99, 1, 'admin', '2025-05-01 10:10:00'),
(103, 'Atomic Habits', 'Book by James Clear', 16.99, 2, 'admin', '2025-05-01 10:10:00'),
(104, 'T-Shirt Men XL', '100% cotton black t-shirt', 12.49, 3, 'admin', '2025-05-01 10:10:00'),
(105, 'Nike Running Shoes', 'Mens Air Zoom Pegasus', 89.99, 5, 'admin', '2025-05-01 10:10:00'),
(106, 'Blender 500W', 'Kitchen blender with 2 jars', 49.99, 4, 'admin', '2025-05-01 10:10:00'),
(107, 'Yoga Mat', '6mm non-slip workout mat', 24.99, 5, 'admin', '2025-05-01 10:10:00'),
(108, 'Kindle Paperwhite', 'E-reader with backlight', 139.99, 2, 'admin', '2025-05-01 10:10:00');

INSERT INTO inventories (inventory_id, product_id, stock_level, stock_threshold, low_stock_bit, last_updated_by, last_updated_at) VALUES
(201, 101, 30, 10, 0, 'admin', '2025-05-01 10:20:00'),
(202, 102, 15, 5, 0, 'admin', '2025-05-01 10:20:00'),
(203, 103, 200, 50, 0, 'admin', '2025-05-01 10:20:00'),
(204, 104, 80, 20, 0, 'admin', '2025-05-01 10:20:00'),
(205, 105, 12, 10, 0, 'admin', '2025-05-01 10:20:00'),
(206, 106, 4, 5, 1, 'admin', '2025-05-01 10:20:00'),
(207, 107, 50, 15, 0, 'admin', '2025-05-01 10:20:00'),
(208, 108, 3, 10, 1, 'admin', '2025-05-01 10:20:00');

INSERT INTO sales (sale_id, sale_date, category_id, product_id, quantity, amount_processed, revenue, last_updated_by, last_updated_at) VALUES
(301, '2025-05-01 11:00:00', 1, 101, 2, 1999.98, 400.00, 'admin', '2025-05-01 11:00:00'),
(302, '2025-05-01 11:30:00', 2, 103, 5, 84.95, 20.00, 'admin', '2025-05-01 11:30:00'),
(303, '2025-05-02 09:15:00', 5, 105, 1, 89.99, 15.00, 'admin', '2025-05-02 09:15:00'),
(304, '2025-05-02 10:00:00', 3, 104, 3, 37.47, 10.00, 'admin', '2025-05-02 10:00:00'),
(305, '2025-05-02 12:20:00', 4, 106, 1, 49.99, 12.00, 'admin', '2025-05-02 12:20:00'),
(306, '2025-05-03 08:00:00', 2, 108, 2, 279.98, 60.00, 'admin', '2025-05-03 08:00:00'),
(307, '2025-05-03 15:00:00', 5, 107, 4, 99.96, 25.00, 'admin', '2025-05-03 15:00:00');
