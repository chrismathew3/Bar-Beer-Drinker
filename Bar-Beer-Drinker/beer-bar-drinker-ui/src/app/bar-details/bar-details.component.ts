import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { BarsService, Bar } from '../bars.service';
import { HttpResponse } from '@angular/common/http';

declare const Highcharts: any;

@Component({
  selector: 'app-bar-details',
  templateUrl: './bar-details.component.html',
  styleUrls: ['./bar-details.component.css']
})
export class BarDetailsComponent implements OnInit {

  barName: string;
  barDetails: Bar;

  constructor(
    private barService: BarsService,
    private route: ActivatedRoute
  ) {
      route.paramMap.subscribe((paramMap) => {

        this.barName = paramMap.get('bar');

        this.barService.getBar(this.barName).subscribe(
          data => {
            this.barDetails = data;
          },
          (error: HttpResponse<any>) => {
            if(error.status === 404){
              alert('Bar not found');
            } else {
              console.error(error.status + ' - ' + error.body);
              alert('An error occurred on the server. ');
            }
          }
        );


        this.barService.getTopDrinkers(this.barName).subscribe(
          data => {
            console.log(data);
            const drinkers = [];
            const counts = [];
            data.forEach(drinker => {
              drinkers.push(drinker.drinker);
              counts.push(drinker.amount);
            });
            this.renderChartTD(drinkers, counts);
          }
        );

        this.barService.getTopBeers(this.barName).subscribe(
          data => {
            console.log(data);
            const beers = [];
            const counts = [];
            data.forEach(beer => {
              beers.push(beer.beer);
              counts.push(beer.quantity);
            });
            this.renderChartTB(beers, counts);
          }
        );

        this.barService.getTopManuf(this.barName).subscribe(
          data => {
            console.log(data);
            const manufacturers = [];
            const counts = [];
            data.forEach(manuf => {
              manufacturers.push(manuf.manuf);
              counts.push(manuf.quantity);
            });
            this.renderChartTM(manufacturers, counts);
          }
        );

      });


  }

  ngOnInit() { }

    renderChartTD(drinkers: string[], counts: number[]) {
      Highcharts.chart('bargraph1', {
        chart: {
          type: 'column'
        },
        title: {
          text: 'Top spenders at this bar'
        },
        xAxis: {
          categories: drinkers,
          title: {
            text: 'Drinker'
          }
        },
        yAxis: {
          min: 0,
          title: {
            text: 'Total Spent'
          },
          labels: {
            overflow: 'justify'
          }
        },
        plotOptions: {
          beer: {
            dataLabels: {
              enabled: true
            }
          }
        },
        legend: {
          enabled: false
        },
        credits: {
          enabled: false
        },
        series: [{
          data: counts
        }]
      });
    }


  renderChartTB(beers: string[], counts: number[]) {
    Highcharts.chart('bargraph2', {
      chart: {
        type: 'column'
      },
      title: {
        text: 'Most Popular Beers at this bar'
      },
      xAxis: {
        categories: beers,
        title: {
          text: 'Beer'
        }
      },
      yAxis: {
        min: 0,
        title: {
          text: 'Total Quantity Bought'
        },
        labels: {
          overflow: 'justify'
        }
      },
      plotOptions: {
        beer: {
          dataLabels: {
            enabled: true
          }
        }
      },
      legend: {
        enabled: false
      },
      credits: {
        enabled: false
      },
      series: [{
        data: counts
      }]
    });
  }

  renderChartTM(manufacturers: string[], counts: number[]) {
    Highcharts.chart('bargraph3', {
      chart: {
        type: 'column'
      },
      title: {
        text: 'Manufacturers who sell the most at this bar'
      },
      xAxis: {
        categories: manufacturers,
        title: {
          text: 'Manuf'
        }
      },
      yAxis: {
        min: 0,
        title: {
          text: 'Total Quantity Bought'
        },
        labels: {
          overflow: 'justify'
        }
      },
      plotOptions: {
        beer: {
          dataLabels: {
            enabled: true
          }
        }
      },
      legend: {
        enabled: false
      },
      credits: {
        enabled: false
      },
      series: [{
        data: counts
      }]
    });
  }

 }
