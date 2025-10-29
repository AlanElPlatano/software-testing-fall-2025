"""
Data-driven tests for the Point of Sale Kata
"""

import pytest

from tdd.pos_kata.pos_kata import PRODUCTS, calculate_total, scan


class TestPOSKata:
    """Tests for individual barcode scans"""

    @pytest.mark.parametrize(
        "barcode,expected",
        [
            ("12345", "$7.25"),
            ("23456", "$12.50"),
            ("99999", "Error: barcode not found"),
            ("", "Error: empty barcode"),
        ],
    )
    def test_scan_single_barcode(self, barcode, expected):
        """Test scanning individual barcodes"""
        assert scan(barcode) == expected

    def test_product_file_loaded(self):
        """Ensure products are loaded correctly"""
        assert "12345" in PRODUCTS
        assert PRODUCTS["12345"] == 7.25

    @pytest.mark.parametrize(
        "barcodes,expected_total",
        [
            (["12345", "23456"], "Total: $19.75"),
            (["12345", "12345"], "Total: $14.50"),
            (["23456"], "Total: $12.50"),
            (["99999"], "Total: $0.00"),  # unknown barcode ignored in total
            ([], "Total: $0.00"),
        ],
    )
    def test_calculate_total(self, barcodes, expected_total):
        """Test total calculation for multiple barcodes"""
        assert calculate_total(barcodes) == expected_total

    def test_total_with_mixed_valid_and_invalid(self):
        """Test total calculation with a mix of valid and invalid barcodes"""
        barcodes = ["12345", "99999", "23456"]
        assert calculate_total(barcodes) == "Total: $19.75"
