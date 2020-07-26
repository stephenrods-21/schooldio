import {Component, OnInit} from '@angular/core';
import {HttpClient} from '@angular/common/http';

declare interface TableData {
    headerRow: string[];
    dataRows: string[][];
}

@Component({
    selector: 'app-table-cmp',
    moduleId: module.id,
    templateUrl: 'table.component.html'
})

export class TableComponent implements OnInit {
    public tableData1: TableData;
    public tableData2: TableData;

    constructor(private $http: HttpClient) {
    }

    ngOnInit() {

        this.$http.get('http://localhost:8000/api/students/').subscribe((result: any) => {
            console.log(result);
            this.tableData1 = {
                headerRow: ['#', 'First Name', 'Last Name', 'student_number'],
                dataRows: result.results
            };
        });


        // this.tableData2 = {
        //     headerRow: ['ID', 'Name', 'Salary', 'Country', 'City'],
        //     dataRows: [
        //         ['1', 'Dakota Rice', '$36,738', 'Niger', 'Oud-Turnhout'],
        //         ['2', 'Minerva Hooper', '$23,789', 'Curaçao', 'Sinaai-Waas'],
        //         ['3', 'Sage Rodriguez', '$56,142', 'Netherlands', 'Baileux'],
        //         ['4', 'Philip Chaney', '$38,735', 'Korea, South', 'Overland Park'],
        //         ['5', 'Doris Greene', '$63,542', 'Malawi', 'Feldkirchen in Kärnten'],
        //         ['6', 'Mason Porter', '$78,615', 'Chile', 'Gloucester']
        //     ]
        // };
    }
}
