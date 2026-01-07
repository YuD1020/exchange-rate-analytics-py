def test_save_and_list_monthly_average(db):
    from app.services.monthly_average_service import MonthlyAverageService

    service = MonthlyAverageService(db)

    service.save("2024-01", 3.72)
    service.save("2024-02", 3.75)

    results = service.list_all()

    assert len(results) == 2
    assert results[0].month == "2024-01"
