import folium
from .models import Scan

def generate_scan_map():
    scans = Scan.objects.all()
    fmap = folium.Map(location=[20, 77], zoom_start=5) if not scans else folium.Map(location=[scans[0].latitude, scans[0].longitude], zoom_start=5)
    
    for scan in scans:
        popup_html = f"""
        <b>{scan.product.name}</b><br>
        {scan.scan_time.strftime('%Y-%m-%d %H:%M:%S')}<br>
        """
        if scan.product.image:
            popup_html += f"<img src='{scan.product.image.url}' width='100'>"
        folium.Marker(
            location=[scan.latitude, scan.longitude],
            popup=popup_html
        ).add_to(fmap)
    
    fmap.save("dashboard/templates/dashboard/map.html")
