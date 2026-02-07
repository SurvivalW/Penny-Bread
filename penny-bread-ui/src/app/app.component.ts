import { Component, ChangeDetectorRef } from '@angular/core';
import { SearchComponent } from './pages/search/search.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [SearchComponent],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  location = 'Wright State University, Dayton OH';

  defaultGif = 'assets/penny_main_transparent.gif';
  kissGif = 'assets/penny_kiss_transparent.gif'

  currentGif = this.defaultGif;

  constructor(private cdr: ChangeDetectorRef) {}

  playKissGif() {
    this.currentGif = this.kissGif;

    setTimeout(() => {
      this.currentGif = this.defaultGif;
      this.cdr.detectChanges();
    }, 2000);
  }
}


