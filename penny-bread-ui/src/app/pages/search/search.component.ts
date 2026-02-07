import { Component, Input, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common'; 
import { FormsModule } from '@angular/forms';  
import { PriceService } from '../../services/price.service';

@Component({
  selector: 'app-search',
  standalone: true,  
  imports: [CommonModule, FormsModule], 
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css'],
  providers: [PriceService]
})
export class SearchComponent {
  @Input() location: string = '';
  searchQuery = '';
  products: any[] = [];
  hasSearched = false;

  stores = ["Walmart", "Sam's Club", "Kroger", "Meijer", "Target"];
  selectedStores: string[] = [];

  constructor(private priceService: PriceService, private cdr: ChangeDetectorRef) {}

  selectStore(store: string) {
    if (this.selectedStores.includes(store)) {
      this.selectedStores = this.selectedStores = this.selectedStores.filter(s => s !== store);
    } else {
      this.selectedStores.push(store);
    }
  }

  filteredProducts() {
  const q = this.searchQuery.trim().toLowerCase();

  return this.products.filter((p: any) => {
    const matchesQuery =
      !q || (p.product_name ?? "").toLowerCase().includes(q);

    const matchesStore =
      this.selectedStores.length === 0 ||
      this.selectedStores.includes(p.store_name);

    return matchesQuery && matchesStore;
  });
}


  onSearch() {
    this.hasSearched = true;
    this.priceService.searchProducts(this.searchQuery).subscribe(data => {
      this.products = data;
      this.cdr.detectChanges();
    });
  }
}