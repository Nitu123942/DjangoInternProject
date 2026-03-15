import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "modular_entity_project.settings")
django.setup()

from vendor.models import Vendor
from product.models import Product
from course.models import Course
from certification.models import Certification
from vendor_product_mapping.models import VendorProductMapping
from product_course_mapping.models import ProductCourseMapping
from course_certification_mapping.models import CourseCertificationMapping

# --- Master Data ---
v1 = Vendor.objects.create(name="Vendor A", code="V001")
v2 = Vendor.objects.create(name="Vendor B", code="V002")

p1 = Product.objects.create(name="Product X", code="P001")
p2 = Product.objects.create(name="Product Y", code="P002")

c1 = Course.objects.create(name="Course Alpha", code="C001")
c2 = Course.objects.create(name="Course Beta", code="C002")

cert1 = Certification.objects.create(name="Cert 101", code="CERT001")
cert2 = Certification.objects.create(name="Cert 102", code="CERT002")

# --- Mappings ---
VendorProductMapping.objects.create(vendor=v1, product=p1, primary_mapping=True)
VendorProductMapping.objects.create(vendor=v2, product=p2, primary_mapping=True)

ProductCourseMapping.objects.create(product=p1, course=c1, primary_mapping=True)
ProductCourseMapping.objects.create(product=p2, course=c2, primary_mapping=True)

CourseCertificationMapping.objects.create(course=c1, certification=cert1, primary_mapping=True)
CourseCertificationMapping.objects.create(course=c2, certification=cert2, primary_mapping=True)

print("✅ Seed data created successfully!")