//
//  Communicator.m
//  Bastion
//
//  Created by Eli Mattson on 10/26/13.
//  Copyright (c) 2013 Eli Mattson. All rights reserved.
//

#import "Communicator.h"
#import "NSData+Base64.h"

@implementation Communicator

#define base @"http://localhost:5000/get_sspng/"
//@"http://54.201.101.85:8080/"

-(NSURLRequest *) sendWebRequest: (NSString *) address {
    NSLog(@"made it this far");
    NSLog(@"Address requested is: %@", address);
    NSData *data = [address dataUsingEncoding:NSASCIIStringEncoding];
    NSString *encodedURL = [data base64EncodedString];
    NSLog(@"encoded string is: %@", encodedURL);
    NSString *fullURL = base;
    fullURL = [fullURL stringByAppendingString:encodedURL];
    NSLog(@"fullUrl is %@", fullURL);
    NSURL *url = [NSURL URLWithString:fullURL];
    NSURLRequest *req = [NSURLRequest requestWithURL:url];
    
    return req;
}

-(NSObject *) getWebsite {
    //get website picture/image and pass it on
    return nil;
}

-(NSObject *) getActionFramework {
    //get action framework (hashtable structure)
    return nil;
}

-(void) sendAction:(NSObject *)userAction {
    //send user action back to
}

@end