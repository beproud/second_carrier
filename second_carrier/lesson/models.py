from django.db import models


class Coach(models.Model):
    """ コーチ
    https://tracery.jp/s/154f89acc9b94282b66bf1d1689d8b06
    レッスンや指導を実施するコーチを表す。
    """

    last_name = models.CharField(verbose_name="姓", max_length=255)
    first_name = models.CharField(verbose_name="名前", max_length=255)
    #: 計算されたレビューポイントが格納される (小数点第1位まで)
    review_point = models.FloatField(verbose_name="レビューポイント", default=0)
    created_at = models.DateTimeField(verbose_name="作成日時")
    updated_at = models.DateTimeField(verbose_name="更新日時")

    class Meta:
        verbose_name = "コーチ"
        db_table = "coach"


class Student(models.Model):
    """ 生徒
    https://tracery.jp/s/9555f6e653fe4872af1edc635cb5cb3c
    レッスンを受講する生徒。
    """

    last_name = models.CharField(verbose_name="姓", max_length=255)
    first_name = models.CharField(verbose_name="名前", max_length=255)
    created_at = models.DateTimeField(verbose_name="作成日時")
    updated_at = models.DateTimeField(verbose_name="更新日時")

    class Meta:
        verbose_name = "生徒"
        db_table = "student"


class LessonRequest(models.Model):
    """ レッスン依頼
    https://tracery.jp/s/1f45aba031ec4f6b8f60bef5d2a5a024
    生徒からコーチへのレッスン依頼
    """

    student = models.ForeignKey("Student", on_delete=models.DO_NOTHING, verbose_name="生徒id")
    coach = models.ForeignKey("Coach", on_delete=models.DO_NOTHING, verbose_name="コーチid")
    lesson_start = models.DateTimeField(verbose_name="レッスン開始予定日時")
    lesson_end = models.DateTimeField(verbose_name="レッスン終了予定日時")
    #: - 0:レッスン依頼中
    #: - 1:レッスン承諾
    #: - 2:レッスン却下
    status = models.SmallIntegerField(verbose_name="ステータス")
    created_at = models.DateTimeField(verbose_name="作成日時")
    updated_at = models.DateTimeField(verbose_name="更新日時")

    class Meta:
        verbose_name = "レッスン依頼"
        db_table = "lesson_request"


class Category(models.Model):
    """ カテゴリ
    https://tracery.jp/s/5655c28ea30c40c39f95fbe8d4487eaa
    スポーツのカテゴリ。
    """

    name = models.CharField(verbose_name="名前", max_length=255)
    created_at = models.DateTimeField(verbose_name="作成日時")
    updated_at = models.DateTimeField(verbose_name="更新日時")

    class Meta:
        verbose_name = "カテゴリ"
        db_table = "category"


class Lesson(models.Model):
    """ レッスン
    https://tracery.jp/s/f6dd78fb8aff4ae29ad08d799b89fd44
    レッスンの予約を表す
    """

    student = models.ForeignKey("Student", on_delete=models.DO_NOTHING, verbose_name="生徒id")
    coach_id = models.IntegerField(verbose_name="コーチid")
    lesson_start = models.DateTimeField(verbose_name="レッスン開始予定日時")
    lesson_end = models.DateTimeField(verbose_name="レッスン終了予定日時")
    created_at = models.DateTimeField(verbose_name="作成日時")
    updated_at = models.DateTimeField(verbose_name="更新日時")

    class Meta:
        verbose_name = "レッスン"
        db_table = "lesson"
